%define	fversion	0.3

%define svn	0
%if %svn
%define release	%mkrel 0.%svn.1
%else
%define release	%mkrel 1
%endif

Summary:	Python bindings for Pigment
Name:		pigment-python
Version:	0.3.2
Release:	%{release}
%if %svn
Source0:	%{name}-%{svn}.tar.bz2
%else
Source0:	http://elisa.fluendo.com/static/download/pigment/%{name}-%{version}.tar.gz
%endif
License:	LGPLv2+
Group:		Development/Python
URL:		http://elisa.fluendo.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
%if %svn
BuildRequires:	autoconf
%endif
BuildRequires:	libgstreamer0.10-devel
BuildRequires:	libgstreamer0.10-plugins-base-devel
BuildRequires:	gstreamer0.10-python
BuildRequires:	glib2-devel
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	python-devel
BuildRequires:	python-gobject
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
%if %svn
%setup -q -n %{name}
%else
%setup -q
%endif

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
%{_datadir}/%{name}/%{fversion}/examples
