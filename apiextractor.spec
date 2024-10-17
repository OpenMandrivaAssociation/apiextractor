Name:		apiextractor
Version:	0.10.10
Release:	1
License:	GPLv2
Summary:	PySide
Group:		Development/KDE and Qt
URL:		https://www.pyside.org
Source0:	http://www.pyside.org/files/%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	libxml2-devel >= 2.6.32
BuildRequires:	libxslt-devel >= 1.1.19

%description
The API Extractor library is used by the binding generator to parse headers
of a given library and merge this data with information provided by
typesystem (XML) files, resulting in a representation of how the API should
be exported to the chosen target language. The generation of source code for
the bindings is performed by specific generators using the API Extractor
library. The API Extractor is based on QtScriptGenerator code.

#------------------------------------------------------------------------------

%define major 0
%define libname %mklibname apiextractor %{major}

%package -n %{libname}
Summary:	apiextractor main library
Group:		System/Libraries

%description -n %{libname}
The API Extractor library is used by the binding generator to parse headers
of a given library and merge this data with information provided by
typesystem (XML) files, resulting in a representation of how the API should
be exported to the chosen target language. The generation of source code for
the bindings is performed by specific generators using the API Extractor
library. The API Extractor is based on QtScriptGenerator code.

%files -n %{libname}
%{_libdir}/libapiextractor.so.%{major}*

#------------------------------------------------------------------------------

%define libnamedev %mklibname apiextractor -d

%package -n %{libnamedev}
Summary:	apiextractor devel files
Group:		System/Libraries
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}
Provides:	libapiextractor-devel = %{version}

%description -n %{libnamedev}
The API Extractor library is used by the binding generator to parse headers
of a given library and merge this data with information provided by
typesystem (XML) files, resulting in a representation of how the API should
be exported to the chosen target language. The generation of source code for
the bindings is performed by specific generators using the API Extractor
library. The API Extractor is based on QtScriptGenerator code.

%files -n %{libnamedev}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/*
%{_includedir}/*

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%__sed 's/-Wno-strict-aliasing/-fno-strict-aliasing/' -i CMakeLists.txt
%cmake
%make

%install
%makeinstall_std -C build


%changelog
* Sat Apr 07 2012 Andrey Bondrov <abondrov@mandriva.org> 0.10.10-1
+ Revision: 789624
- Fix description length
- New version 0.10.10

* Tue Oct 25 2011 Andrey Bondrov <abondrov@mandriva.org> 0.10.8-1
+ Revision: 707131
- New version 0.10.8

* Thu Sep 29 2011 Andrey Bondrov <abondrov@mandriva.org> 0.10.7-1
+ Revision: 701871
- New version: 0.10.7

* Tue Sep 20 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.10.6-1
+ Revision: 700468
- haul out some rpm trash
- new version

* Thu Jul 14 2011 Lev Givon <lev@mandriva.org> 0.10.4-1
+ Revision: 689935
- Update to 0.10.4.

* Wed Jul 13 2011 Lev Givon <lev@mandriva.org> 0.10.3-3
+ Revision: 689904
- Fix release tag.

* Wed Jun 08 2011 Paulo Belloni <paulo@mandriva.com> 0.10.3-2
+ Revision: 683169
- Fixing no-strict-aliasing flag. We need to inform upstream.

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.10.3-1
+ Revision: 680396
- update to new version 0.10.3

* Sun May 01 2011 Funda Wang <fwang@mandriva.org> 0.10.2-1
+ Revision: 661146
- update to new version 0.10.2

* Sat Apr 02 2011 Funda Wang <fwang@mandriva.org> 0.10.1-1
+ Revision: 649940
- update to new version 0.10.1

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 0.10.0-1
+ Revision: 640459
- update to new version 0.10.0

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 0.9.4-2
+ Revision: 640448
- rebuild to obsolete old packages

* Thu Feb 03 2011 Funda Wang <fwang@mandriva.org> 0.9.4-1
+ Revision: 635672
- update to new version 0.9.4

* Sat Jan 29 2011 Funda Wang <fwang@mandriva.org> 0.9.3-1
+ Revision: 633802
- update to new version 0.9.3

* Tue Jan 18 2011 Funda Wang <fwang@mandriva.org> 0.9.2-1
+ Revision: 631520
- update to new version 0.9.2

* Mon Dec 20 2010 Funda Wang <fwang@mandriva.org> 0.9.1-1mdv2011.0
+ Revision: 623331
- new version 0.9.1

* Sat Nov 27 2010 Funda Wang <fwang@mandriva.org> 0.9.0-1mdv2011.0
+ Revision: 601805
- update to new version 0.9.0

* Thu Oct 14 2010 Funda Wang <fwang@mandriva.org> 0.8.1-1mdv2011.0
+ Revision: 585662
- update to new version 0.8.1

* Wed Sep 22 2010 Funda Wang <fwang@mandriva.org> 0.8.0-1mdv2011.0
+ Revision: 580560
- update to new version 0.8.0

* Thu Aug 05 2010 Funda Wang <fwang@mandriva.org> 0.7.0-1mdv2011.0
+ Revision: 566322
- drop unused BR
- new version 0.7.0

* Wed Feb 03 2010 Funda Wang <fwang@mandriva.org> 0.3.3-1mdv2010.1
+ Revision: 500107
- New version 0.3.3

* Fri Sep 25 2009 Helio Chissini de Castro <helio@mandriva.com> 0.3-2mdv2010.0
+ Revision: 448952
- Fix install path for cmake files
- New upstream version

* Fri Aug 21 2009 Helio Chissini de Castro <helio@mandriva.com> 0.2-2mdv2010.0
+ Revision: 419348
- Correct license

* Thu Aug 20 2009 Helio Chissini de Castro <helio@mandriva.com> 0.2-1mdv2010.0
+ Revision: 418561
- imported package apiextractor


