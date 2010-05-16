# TODO:
# - system prototype.js, scriptaculous.js
Summary:	Simple, unobtrusive script used to overlay images on the webpage
Name:		lightbox
Version:	2.04
Release:	0.4
License:	Creative Commons Attribution 2.5
Group:		Applications/WWW
Source0:	http://www.lokeshdhakar.com/projects/lightbox2/releases/%{name}%{version}.zip
# Source0-md5:	c930f97a5791f202d7c48303de36f282
Patch0:		%{name}-url.patch
URL:		http://www.lokeshdhakar.com/projects/lightbox2/
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	unzip
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

%patch0 -p1

cat > apache.conf <<'EOF'
Alias /%{name} %{_appdir}
<Directory %{_appdir}>
	Allow from all
</Directory>
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_appdir}}
cp -a %{name}/* $RPM_BUILD_ROOT%{_appdir}

cp -a apache.conf $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf
cp -a apache.conf $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- apache1 < 1.3.37-3, apache1-base
%webapp_register apache %{_webapp}

%triggerun -- apache1 < 1.3.37-3, apache1-base
%webapp_unregister apache %{_webapp}

%triggerin -- apache < 2.2.0, apache-base
%webapp_register httpd %{_webapp}

%triggerun -- apache < 2.2.0, apache-base
%webapp_unregister httpd %{_webapp}

%files
%defattr(644,root,root,755)
%dir %attr(750,root,http) %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf
%{_appdir}
