%include	/usr/lib/rpm/macros.perl
Summary:	Yet Another Part-of-Speech and Morphological Analyzer
Summary(pl.UTF-8):	Jeszcze jeden analizator części mowy i morfologii
Name:		mecab
Version:	0.996
Release:	2
License:	GPL v2 or LGPL v2.1 or BSD
Group:		Libraries
#Source0Download: https://taku910.github.io/mecab
# 0.996 can be found at https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7cENtOXlicTFaRUE
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	7603f8975cea2496d88ed62545ba973f
Patch0:		%{name}-libexec.patch
URL:		https://taku910.github.io/mecab
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yet Another Part-of-Speech and Morphological Analyzer.

%description -l pl.UTF-8
Jeszcze jeden analizator części mowy i morfologii.

%package devel
Summary:	Header files for MeCab
Summary(pl.UTF-8):	Pliki nagłówkowe MeCab
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for MeCab.

%description devel -l pl.UTF-8
Pliki nagłówkowe MeCab.

%package static
Summary:	Static MeCab library
Summary(pl.UTF-8):	Statyczna biblioteka MeCab
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static MeCab library.

%description static -l pl.UTF-8
Statyczna biblioteka MeCab.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub .
%configure

%{__make} \
	CFLAGS="%{rpmcflags} -Wall" \
	CXXFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/mecab/dic

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BSD COPYING README doc/*.html
%attr(755,root,root) %{_bindir}/mecab
%attr(755,root,root) %{_libdir}/libmecab.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmecab.so.2
%dir %{_libexecdir}/mecab
%attr(755,root,root) %{_libexecdir}/mecab/mecab-cost-train
%attr(755,root,root) %{_libexecdir}/mecab/mecab-dict-gen
%attr(755,root,root) %{_libexecdir}/mecab/mecab-dict-index
%attr(755,root,root) %{_libexecdir}/mecab/mecab-system-eval
%attr(755,root,root) %{_libexecdir}/mecab/mecab-test-gen
%if "%{_libdir}" != "%{_libexecdir}"
%dir %{_libdir}/mecab
%endif
%dir %{_libdir}/mecab/dic
%{_mandir}/man1/mecab.1*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mecabrc

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mecab-config
%attr(755,root,root) %{_libdir}/libmecab.so
%{_libdir}/libmecab.la
%{_includedir}/mecab.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libmecab.a
