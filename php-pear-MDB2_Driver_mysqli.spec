%define		_status		beta
%define		_pearname	MDB2_Driver_mysqli
%define		subver	b4
%define		rel		1
Summary:	%{_pearname} - mysqli MDB2 driver
Summary(pl.UTF-8):	%{_pearname} - sterownik mysqli dla MDB2
Name:		php-pear-%{_pearname}
Version:	1.5.0
Release:	0.%{subver}.%{rel}
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{subver}.tgz
# Source0-md5:	4f65358cf74e98d645b66dd575e810ff
URL:		http://pear.php.net/package/MDB2_Driver_mysqli/
BuildRequires:	php-pear-PEAR >= 1:1.9.1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 5.0.0
Requires:	php(mysqli)
Requires:	php-pear
Requires:	php-pear-MDB2 >= 1:2.5.0-0.b4
Obsoletes:	php-pear-MDB2_Driver_mysqli-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the MySQLi MDB2 driver.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Sterownik MySQLi dla MDB2.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/MDB2/Driver/Datatype/mysqli.php
%{php_pear_dir}/MDB2/Driver/Manager/mysqli.php
%{php_pear_dir}/MDB2/Driver/Native/mysqli.php
%{php_pear_dir}/MDB2/Driver/Reverse/mysqli.php
%{php_pear_dir}/MDB2/Driver/mysqli.php
%{php_pear_dir}/MDB2/Driver/Function/mysqli.php
%{php_pear_dir}/data/MDB2_Driver_mysqli
