%define	fversion	0.3

Summary:	Python bindings for Pigment
Name:		pigment-python
Version:	0.3.12
Release:	4
Source0:	http://elisa.fluendo.com/static/download/pigment/%{name}-%{version}.tar.bz2
License:	LGPLv2+
Group:		Development/Python
URL:		https://elisa.fluendo.com/
BuildRequires:	pkgconfig(gstreamer-0.10)
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:	gstreamer0.10-python
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	python-devel
BuildRequires:	python-gobject
BuildRequires:	python-pyxml
BuildRequires:	pygtk2.0-devel
BuildRequires:	pkgconfig(pigment-0.3)
Requires:	pigment

%description
Python bindings for the Pigment library.

%package devel
Group:		Development/Python
Summary:	Development headers for pigment-python
Requires:	%{name}
Requires:	pkgconfig(pigment-0.3)

%description devel
Python bindings for the Pigment library.

%prep
%setup -q

%build
%configure2_5x
make

%install
%makeinstall_std

%files
%{py_puresitedir}/pgm
%{py_platsitedir}/*.so

%files devel
%{_datadir}/%{name}

