%define major	1
%define oname	ptp2
%define libname %mklibname %{oname}_ %{major}
%define devname %mklibname %{oname} -d

%define _disable_lto 1

Summary:	Library to access digital cameras via PTP
Name:		libptp2
Version:	1.1.10
Release:	14
License:	GPL
Group:		Graphics
Url:		http://sourceforge.net/projects/libptp/
Source0:	http://heanet.dl.sourceforge.net/sourceforge/libptp/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(libusb)

%description
Many digital cameras communicate with computers via the Picture
Transfer Protocol (PTP). This protocol gives a standardized
manufacturer-independent set of camera operation commands, as
downloading pictures, remote capturing, ... Unfortunately
manufacturers added also there own non-standard commands, especially
for remote control. This library contains a near complete remote
control command set for Canon digital cameras and also some stuff for
Nikon.

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

%package -n %{libname}
Summary:	Library to access digital cameras via PTP
Group:		Graphics
Provides:	%{name}

%description -n %{libname}
Many digital cameras communicate with computers via the Picture
Transfer Protocol (PTP). This protocol gives a standardized
manufacturer-independent set of camera operation commands, as
downloading pictures, remote capturing, ... Unfortunately
manufacturers added also there own non-standard commands, especially
for remote control. This library contains a near complete remote
control command set for Canon digital cameras and also some stuff for
Nikon.

%package -n %{devname}
Summary: 	Headers and links to compile against the "%{libname}" library
Group:		Graphics
Requires: 	%{libname} = %{version}
Provides:	libptp2-devel
Obsoletes:	%{_lib}%{oname}_1-devel

%description -n %{devname}
This package contains all files which one needs to compile programs using
the "%{libname}" library.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

# Not safe for -j24 as of 1.1.10
make

%install
%makeinstall_std

%find_lang %{name} || touch %{name}.lang

%files -n ptpcam
%doc AUTHORS COPYING ChangeLog README TODO
%{_bindir}/*

%files -n %{libname} -f %{name}.lang
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_libdir}/*.so
%{_includedir}/*

