%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	Parser
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - XML parsing class based on PHP's bundled expat
Summary(pl.UTF-8):	%{_pearname} - klasa analizującą XML przy użyciu expat
Name:		php-pear-%{_pearname}
Version:	1.2.8
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	93ca92f503f1d921c9520a140bcff270
URL:		http://pear.php.net/package/XML_Parser/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-PEAR-core
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an XML parser based on PHP's built-in xml extension. It
supports two basic modes of operation: "func" and "event". In "func"
mode, it will look for a function named after each element
(xmltag_ELEMENT for start tags and xmltag_ELEMENT_ for end tags), and
in "event" mode it uses a set of generic callbacks.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet zawiera klasę analizującą XML opartą na wbudowanym w PHP
rozszerzeniu xml. Klasa ta obsługuje dwa podstawowe tryby pracy:
"func" oraz "event". W trybie "func" szuka funkcji o nazwach
odpowiadających każdemu elementowi (xmltag_ELEMENT dla znaczników
początkowych i xmltag_ELEMENT_ dla znaczników końcowych), natomiast w
trybie "event" używa zestawu ogólnych callbacków.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

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
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
