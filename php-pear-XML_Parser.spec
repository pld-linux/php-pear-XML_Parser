%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	Parser
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - XML parsing class based on PHP's bundled expat
Summary(pl):	%{_pearname} - klasa analizuj±c± XML przy u¿yciu expat
Name:		php-pear-%{_pearname}
Version:	1.2.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	602c42a31056801c8621bed93da78e84
URL:		http://pear.php.net/package/XML_Parser/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an XML parser based on PHP's built-in xml extension. It
supports two basic modes of operation: "func" and "event". In "func"
mode, it will look for a function named after each element
(xmltag_ELEMENT for start tags and xmltag_ELEMENT_ for end tags), and
in "event" mode it uses a set of generic callbacks.

In PEAR status of this package is: %{_status}.

%description -l pl
Ten pakiet zawiera klasê analizuj±c± XML opart± na wbudowanym w PHP
rozszerzeniu xml. Klasa ta obs³uguje dwa podstawowe tryby pracy:
"func" oraz "event". W trybie "func" szuka funkcji o nazwach
odpowiadaj±cych ka¿demu elementowi (xmltag_ELEMENT dla znaczników
pocz±tkowych i xmltag_ELEMENT_ dla znaczników koñcowych), natomiast w
trybie "event" u¿ywa zestawu ogólnych callbacków.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/tests/*
%{php_pear_dir}/%{_class}/*.php
