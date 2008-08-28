# TODO:
# - system prototype.js, scriptaculous.js
Summary:	Simple, unobtrusive script used to overlay images on the webpage
Name:		lightbox
Version:	2.04
Release:	0.2
License:	GPL
Group:		Applications/WWW
Source0:	http://www.lokeshdhakar.com/projects/lightbox2/releases/%{name}%{version}.zip
# Source0-md5:	c930f97a5791f202d7c48303de36f282
URL:		http://www.lokeshdhakar.com/projects/lightbox2/
BuildRequires:	rpmbuild(macros) >= 1.268
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_sysconfdir	%{_webapps}/%{_webapp}
%define		_appdir		%{_datadir}/%{_webapp}

%description
Lightbox is a simple, unobtrusive script used to overlay images on the
current page. It's a snap to setup and works on all modern browsers.

%prep
%setup -qc
%{__sed} -i -e 's,\r$,,' *.html
install -d %{name}
mv css images js *.html %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a %{name}/* $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
