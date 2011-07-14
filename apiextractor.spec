Name: apiextractor
Version: 0.10.4
Release: %mkrel 1
License: GPLv2
Summary: PySide
Group: Development/KDE and Qt
URL: http://www.pyside.org
Source0:  http://www.pyside.org/files/%name-%version.tar.bz2
Patch0: apiextractor-0.3.3-cmake-module-install.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: cmake
BuildRequires: qt4-devel
BuildRequires: libxml2-devel >= 2.6.32
BuildRequires: libxslt-devel >= 1.1.19

%description
The API Extractor library is used by the binding generator to parse headers of a
given library and merge this data with information provided by typesystem (XML)
files, resulting in a representation of how the API should be exported to the 
chosen target language. The generation of source code for the bindings is performed 
by specific generators using the API Extractor library.
The API Extractor is based on QtScriptGenerator code.

#------------------------------------------------------------------------------

%define major 0
%define libname %mklibname apiextractor %{major}

%package -n %{libname}
Summary: apiextractor main library
Group: System/Libraries

%description -n %{libname}
The API Extractor library is used by the binding generator to parse headers of a
given library and merge this data with information provided by typesystem (XML)
files, resulting in a representation of how the API should be exported to the 
chosen target language. The generation of source code for the bindings is performed 
by specific generators using the API Extractor library.
The API Extractor is based on QtScriptGenerator code.

%files -n %{libname}
%defattr(-,root,root,-)
%_libdir/libapiextractor.so.%{major}*

#------------------------------------------------------------------------------

%define libnamedev %mklibname apiextractor -d

%package -n %{libnamedev}
Summary: apiextractor devel files
Group: System/Libraries
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}
Provides: libapiextractor-devel = %{version}

%description -n %{libnamedev}
The API Extractor library is used by the binding generator to parse headers of a
given library and merge this data with information provided by typesystem (XML)
files, resulting in a representation of how the API should be exported to the 
chosen target language. The generation of source code for the bindings is performed 
by specific generators using the API Extractor library.
The API Extractor is based on QtScriptGenerator code.

%files -n %{libnamedev}
%defattr(-,root,root,-)
%_libdir/*.so
%_libdir/pkgconfig/*
%_libdir/cmake/*
%_includedir/*

#------------------------------------------------------------------------------

%prep
%setup -q

%build
sed 's/-Wno-strict-aliasing/-fno-strict-aliasing/' -i CMakeLists.txt
%cmake
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean
rm -rf %buildroot

