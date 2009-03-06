%define	fversion	0.3

%define rel	1
%define svn	0
%if %svn
%define release		%mkrel 0.%svn.%rel
%define distname	%{name}-%{svn}.tar.lzma
%define dirname		%{name}
%else
%define release		%mkrel %rel
%define distname	%{name}-%{version}.tar.bz2
%define dirname		%{name}-%{version}
%endif

Summary:	Python bindings for Pigment
Name:		pigment-python
Version:	0.3.10
Release:	%{release}
Source0:	http://elisa.fluendo.com/static/download/pigment/%{distname}
License:	LGPLv2+
Group:		Development/Python
URL:		http://elisa.fluendo.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libgstreamer-devel >= 0.10
BuildRequires:	libgstreamer0.10-plugins-base-devel
BuildRequires:	gstreamer0.10-python
BuildRequires:	glib2-devel
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	python-devel
BuildRequires:	python-gobject
BuildRequires:	python-pyxml
BuildRequires:	pygtk2.0-devel
BuildRequires:	pigment-devel
BuildRequires:	libpigment-devel
Requires:	pigment

%description
Python bindings for the Pigment library.

%package devel
Group:		Development/Python
Summary:	Development headers for pigment-python
Requires:	%{name}
Requires:	pigment-devel
Requires:	libpigment-devel

%description devel
Python bindings for the Pigment library.

%prep
%setup -q -n %{dirname}

%build
%if %svn
./autogen.sh
%endif
%configure2_5x
make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{py_puresitedir}/pgm
%{py_platsitedir}/*.so

%files devel
%defattr(-,root,root)
%{py_platsitedir}/*.la
%{_datadir}/%{name}
