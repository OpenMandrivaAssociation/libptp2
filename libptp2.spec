##### GENERAL STUFF #####
%define release %mkrel 4
%define libname %mklibname ptp2 _1

Summary:	Library to access digital cameras via PTP
Name:		libptp2
Version:	1.1.10
Release:	%release
License:	GPL
Group:		Graphics
Url:		http://sourceforge.net/projects/libptp/

##### SOURCE FILES #####

Source: http://heanet.dl.sourceforge.net/sourceforge/libptp/%{name}-%{version}.tar.gz

##### ADDITIONAL DEFINITIONS #####

BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires:	libusb-devel

##### SUB-PACKAGES #####

%description
Many digital cameras communicate with computers via the Picture
Transfer Protocol (PTP). This protocol gives a standardized
manufacturer-independent set of camera operation commands, as
downloading pictures, remote capturing, ... Unfortunately
manufacturers added also there own non-standard commands, especially
for remote control. This library contains a near complete remote
control command set for Canon digital cameras and also some stuff for
Nikon.

%package -n %libname
Summary:	Library to access digital cameras via PTP
Provides:	%{name}
Group:		Graphics

%description -n %libname
Many digital cameras communicate with computers via the Picture
Transfer Protocol (PTP). This protocol gives a standardized
manufacturer-independent set of camera operation commands, as
downloading pictures, remote capturing, ... Unfortunately
manufacturers added also there own non-standard commands, especially
for remote control. This library contains a near complete remote
control command set for Canon digital cameras and also some stuff for
Nikon.

%package -n %{libname}-devel
Summary: 	Headers and links to compile against the "%{libname}" library
Requires: 	%{libname} = %{version}
Provides:	libptp2-devel
Group:		Graphics

%description -n %{libname}-devel
This package contains all files which one needs to compile programs using
the "%{libname}" library.

%package -n ptpcam
Summary:	Command line utility to access digital cameras via PTP
Group:		Graphics

%description -n ptpcam
Many digital cameras communicate with computers via the Picture
Transfer Protocol (PTP). This protocol gives a standardized
manufacturer-independent set of camera operation commands, as
downloading pictures, remote capturing, ... Unfortunately
manufacturers added also there own non-standard commands, especially
for remote control. ptpcam makes use of the %{libname} library which
contains a near complete remote control command set for Canon digital
cameras and also some stuff for Nikon.


##### PREP #####

%prep
rm -rf $RPM_BUILD_DIR/%{name}-%{version}
%setup -q -n %{name}-%{version}
##### BUILD #####

%build
# "autogen" is needed when we have a CVS snapshot.
#./autogen.sh
%configure
make

##### INSTALL #####

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

# Install the README files of the source tarball in the doc directory
#cp *.txt $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}

%find_lang %{name}

##### PRE/POST INSTALL SCRIPTS #####

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT


##### FILE LISTS FOR ALL BINARY PACKAGES #####

##### libptp2
%files -n %libname -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README TODO
%{_libdir}/*.so.*

##### libptp2-devel
%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_includedir}/*

##### ptpcam
%files -n ptpcam
%defattr(-,root,root)
%{_bindir}/*

##### CHANGELOG #####
