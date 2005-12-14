%include	/usr/lib/rpm/macros.php
%define		_class		MDB2
%define		_subclass	Driver_mysqli
%define		_status		alpha
%define		_pearname	MDB2_Driver_mysqli

Summary:	%{_pearname} - mysqli MDB2 driver
Summary(pl):	%{_pearname} - sterownik mysqli dla MDB2
Name:		php-pear-%{_pearname}
Version:	0.1.1
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	aa3c2090a80cbd832055135dca337cb9
URL:		http://pear.php.net/package/MDB2_Driver_mysqli/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-common >= 3:5.0.0
Requires:	php-pear-PEAR >= 1:1.0b1
Requires:	php-pear-MDB2 >= 2.0.0-0.beta6
Requires:	php-mysqli
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the MySQLi MDB2 driver.
 
In PEAR status of this package is: %{_status}.

%description -l pl
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
%{php_pear_dir}/package_mysqli.php
