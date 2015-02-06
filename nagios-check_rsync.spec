Name:		nagios-check_rsync
Version:	1.02
Release:	7
Summary:    Nagios rsync plugin
License:    GPL
Group:		Networking/Other
Url:        http://exchange.nagios.org/directory/Plugins/Network-Protocols/Rsync/check_rsync/details
Source0:    check_rsync
Requires:   rsync
BuildArch:  noarch

%description
Checks rsync servers availability, as well as (optionally) individual modules
availability. It also supports authentication on modules.

%prep

%build

%install
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

%files 
%{_datadir}/nagios/plugins/check_rsync
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_rsync.cfg
