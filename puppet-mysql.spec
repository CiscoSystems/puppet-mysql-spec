Name:		puppet-mysql	
Version:	0.3
Release:	1cisco%{?dist}
Summary:	Puppet Mysql module

Group:		System Environment/Base
License: 	Apache License 2.0	
URL:		https://github.com/CiscoSystems/puppet-mysql.git
Source0: 	%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%define tmpname %(echo %{name} | cut -d- -f 2-)

%description
This module manages mysql on Linux (RedHat/Debian) distros. A native mysql provider implements database resource type to handle database, database user, and database permission. Pluginsync needs to be enabled for this module to function properly.

%prep
%setup -q


%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/%{_usr}/share/puppet/modules/%{tmpname}/
cp -R * %{buildroot}/%{_usr}/share/puppet/modules/%{tmpname}/

%files
%dir %{_usr}/share/puppet/modules/%{tmpname}/
%{_usr}/share/puppet/modules/%{tmpname}/*


%defattr(-,root,root,-)
%doc README.md CHANGELOG LICENSE

%clean
rm -rf %{buildroot}

%changelog
* Thu May 16 2013 Pradeep Kilambi <pkilambi@cisco.com> 0.3-1cisco
- 

* Tue May 07 2013 Pradeep Kilambi <pkilambi@cisco.com> 0.2-1cisco
- new package built with tito

* Tue Apr 24 2013 Pradeep Kilambi <pkilambi@cisco.com> - 0.1-1cisco
- Initial package.

