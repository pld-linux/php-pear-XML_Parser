%define		_status		stable
%define		_pearname	XML_Parser
Summary:	%{_pearname} - XML parsing class based on PHP's bundled expat
Summary(pl.UTF-8):	%{_pearname} - klasa analizującą XML przy użyciu expat
Name:		php-pear-%{_pearname}
Version:	1.3.8
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	dd83ce08c7471d23d8ba060f18a938fa
URL:		http://pear.php.net/package/XML_Parser/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-PEAR-core
Obsoletes:	php-pear-XML_Parser-tests
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
%{php_pear_dir}/XML/*.php
%{php_pear_dir}/XML/Parser
