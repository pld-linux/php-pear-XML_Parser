%include	/usr/lib/rpm/macros.php
%define         _class          XML
%define         _subclass       Parser
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - XML parsing class based on PHP's bundled expat
Summary(pl):	%{_class}_%{_subclass} -
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
BuildRequires:	rpm-php-pearprov
URL:		http://pear.php.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an XML parser based on PHP's built-in xml extension. It
supports two basic modes of operation: "func" and "event". In "func"
mode, it will look for a function named after each element
(xmltag_ELEMENT for start tags and xmltag_ELEMENT_ for end tags), and
in "event" mode it uses a set of generic callbacks.

%description -l pl

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
cd %{_pearname}-%{version}

install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install *.php			$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/tests/*
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/%{_class}/*.php
