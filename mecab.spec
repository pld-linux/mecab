# TODO: should dictionary (over 60MB) be separated to subpackage or not?
%define	ipadicversion	2.7.0
Summary:	Yet Another Part-of-Speech and Morphological Analyzer
Summary(pl):	Jeszcze jeden analizator czê¶ci mowy i morfologii
Name:		mecab
Version:	0.79
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://cl.aist-nara.ac.jp/~taku-ku/software/mecab/src/%{name}-%{version}.tar.gz
# Source0-md5:	d7d4884f4798d9a88989b0b22953240a
Source1:	http://chasen.aist-nara.ac.jp/stable/ipadic/ipadic-%{ipadicversion}.tar.gz
# Source1-md5:	f36d315cae25b086a889b7090c674977
Patch0:		%{name}-segv.patch
Patch1:		%{name}-libdir.patch
URL:		http://cl.aist-nara.ac.jp/~taku-ku/software/mecab/
BuildRequires:	libstdc++-devel
Requires:	perl >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yet Another Part-of-Speech and Morphological Analyzer.

%description -l pl
Jeszcze jeden analizator czê¶ci mowy i morfologii.

%package devel
Summary:	Header files for MeCab
Summary(pl):	Pliki nag³ówkowe MeCab
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for MeCab.

%description devel -l pl
Pliki nag³ówkowe MeCab.

%package static
Summary:	Static MeCab library
Summary(pl):	Statyczna biblioteka MeCab
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static MeCab library.

%description static -l pl
Statyczna biblioteka MeCab.

%prep
%setup -q
%patch0 -p1

tar xzf %{SOURCE1} -C dic

%patch1 -p1

%build
cp -f /usr/share/automake/config.sub .
%configure

%{__make} \
	CFLAGS="%{rpmcflags} -Wall" \
	CXXFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README doc/*.html
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_libdir}/mecab
%{_mandir}/man1/mecab.1*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/mecabrc

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/mecab.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
