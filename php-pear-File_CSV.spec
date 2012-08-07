%define		status		alpha
%define		pearname	File_CSV
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Read and write of CSV files
Name:		php-pear-%{pearname}
Version:	1.0.0
Release:	2
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	a3899032d51cee860a2008e8b294c885
URL:		http://pear.php.net/package/File_CSV/
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php(pcre)
Requires:	php-pear
Requires:	php-pear-File >= 1.4.0-0.alpha1
Requires:	php-pear-PEAR-core >= 1:1.7.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Read and write of CSV files as well as discovering the format the CSV
file is in.

Supports headers and is excel compatible, i.e. ="0004" outputs as 0004
(only read wise)

For more information on CSV: <http://rfc.net/rfc4180.html>

In PEAR status of this package is: %{status}.

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
%doc docs/File_CSV/FILE_CSV_LICENSE
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/File/CSV.php
