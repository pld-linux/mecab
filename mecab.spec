Summary:	Yet Another Part-of-Speech and Morphological Analyzer
Summary(pl):	Jeszcze jeden analizator czê¶ci mowy i morfologii
Name:		mecab
Version:	0.76
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://cl.aist-nara.ac.jp/~taku-ku/software/mecab/src/%{name}-%{version}.tar.gz
# Source0-md5:	c312f2e218f6857dc487662c379d0f6e
#%define ipadicversion 2.6.0
#Source1: ipadic-%{ipadicversion}.tar.gz
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
Requires:	%{name} = %{version}
Requires:	libstdc++-devel

%description devel
Header files for MeCab.

%description devel -l pl
Pliki nag³ówkowe MeCab.

%package static
Summary:	Static MeCab library
Summary(pl):	Statyczna biblioteka MeCab
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static MeCab library.

%description static -l pl
Statyczna biblioteka MeCab.

%prep
%setup -q

%build
#ln -s ../../ipadic-%{ipadicversion} dic/ipadic-%{ipadicversion}
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
