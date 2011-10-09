Summary:	Command line pastebin
Summary(pl.UTF-8):	Klient pastebin działający z linii poleceń
Name:		pastebin-cl
Version:	0.6
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	https://github.com/tupton/pastebin-cl/zipball/0.6#/%{name}-%{version}.zip
# Source0-md5:	9f638e89a6b1a8e66395615a11234c03
URL:		https://github.com/tupton/pastebin-cl
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A utility to paste to pastebin from the command line.

%description -l pl
Narzędzie do wklejania do pastebin z linii poleceń.

%prep
%setup -q -n tupton-%{name}-dedeadf

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install pastebin.py $RPM_BUILD_ROOT%{_bindir}/pastebin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pastebin
