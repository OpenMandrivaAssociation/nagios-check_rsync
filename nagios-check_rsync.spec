%define name	nagios-check_rsync
%define version	1.02
%define release	%mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    Nagios rsync plugin
License:    GPL
Group:		Networking/Other
Url:        http://www.nagiosexchange.org/cgi-bin/page.cgi?g=Detailed%2F2094.html
Source0:    check_rsync
Requires:   rsync
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Checks rsync servers availability, as well as (optionally) individual modules
availability. It also supports authentication on modules.

%prep

%build

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/nagios/plugins
install -m 755 %{SOURCE0} %{buildroot}%{_datadir}/nagios/plugins

perl -pi -e 's|/usr/local/nagios/libexec|%{_datadir}/nagios/plugins|' \
    %{buildroot}%{_datadir}/nagios/plugins/check_rsync

install -d -m 755 %{buildroot}%{_sysconfdir}/nagios/plugins.d
cat > %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_rsync.cfg <<'EOF'
define command{
	command_name	check_rsync
	command_line	%{_datadir}/nagios/plugins/check_rsync -H $HOSTADDRESS$
}
EOF

%clean
rm -rf %buildroot

%files 
%defattr(-,root,root)
%{_datadir}/nagios/plugins/check_rsync
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_rsync.cfg

