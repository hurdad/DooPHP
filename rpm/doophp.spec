Name:		doophp
Version:	1.5
Release:	1%{?dist}
Summary:	PHP MVC Framework
Group:          System Environment/Libraries 	
License:	BSD
URL:		http://www.doophp.com
Source:		doophp-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
Requires:	php
Requires:	php-cli
Requires:	php-pdo
Requires:	php-mysql
Requires:	php-mbstring
Packager:	Alexander Hurd <hurdad@gmail.com>

%description
high performance open source PHP framework

%prep
%setup -q

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_datadir}/doophp
%{__cp} -av * %{buildroot}%{_datadir}/doophp

%clean
rm -rf %{buildroot}

%post

%postun

%files
%defattr(-,root,root,-)
%doc INSTALL.txt LICENSE.txt CHANGELOG.txt
%{_datadir}/

%changelog

