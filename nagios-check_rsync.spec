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



%changelog
* Sat Dec 11 2010 Oden Eriksson <oeriksson@mandriva.com> 1.02-5mdv2011.0
+ Revision: 620463
- the mass rebuild of 2010.0 packages

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.02-4mdv2010.0
+ Revision: 440226
- rebuild

* Mon Dec 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-3mdv2009.1
+ Revision: 314629
- now a noarch package

* Sat Oct 18 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-2mdv2009.1
+ Revision: 294898
- really use 1.02 source

* Sat Oct 18 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdv2009.1
+ Revision: 294891
- import nagios-check_rsync


* Sat Oct 18 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdv2009.1
- first mdv release
