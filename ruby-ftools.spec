%define	pkgname	ftools
Summary:	Various file-tools for Ruby, that I want to share with others
Name:		ruby-%{pkgname}
Version:	0.0.0
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	dda59770db8a8c129630c671ee2f397e
URL:		http://github.com/kaspernj/ftools
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Various file-tools for Ruby, that I want to share with others

%prep
%setup -q -n %{pkgname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rdoc LICENSE.txt
%{ruby_vendorlibdir}/ftools.rb
