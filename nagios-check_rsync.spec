%define name	nagios-check_rsync
%define version	1.02
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    Nagios rsync plugin
License:    GPL
Group:		Networking/Other
Url:        http://www.nagiosexchange.org/cgi-bin/page.cgi?g=Detailed%2F2094.html
Source0:    check_rsync
Requires:   rsync
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Checks rsync servers availability, as well as (optionally) individual modules
availability. It also supports authentication on modules.

%prep

%build

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_libdir}/nagios/plugins
install -m 755 %{SOURCE0} %{buildroot}%{_libdir}/nagios/plugins

perl -pi -e 's|/usr/local/nagios/libexec|%{_libdir}/nagios/plugins|' \
    %{buildroot}%{_libdir}/nagios/plugins/check_rsync

install -d -m 755 %{buildroot}%{_sysconfdir}/nagios/plugins.d
cat > %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_rsync.cfg <<'EOF'
define command{
	command_name	check_rsync
	command_line	%{_libdir}/nagios/plugins/check_rsync -H $HOSTADDRESS$
}
EOF

%clean
rm -rf %buildroot

%files 
%defattr(-,root,root)
%defattr(-,root,root)
%{_libdir}/nagios/plugins/check_rsync
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_rsync.cfg

