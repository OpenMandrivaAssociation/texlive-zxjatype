# revision 28541
# category Package
# catalog-ctan /language/japanese/zxjatype
# catalog-date 2012-12-15 19:00:17 +0100
# catalog-license other-free
# catalog-version 0.6
Name:		texlive-zxjatype
Version:	0.6
Release:	9
Summary:	Standard conforming typesetting of Japanese, for XeLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/japanese/zxjatype
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zxjatype.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zxjatype.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive zxjatype package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/zxjatype/zxjatype.sty
%doc %{_texmfdistdir}/doc/latex/zxjatype/LICENSE
%doc %{_texmfdistdir}/doc/latex/zxjatype/README
%doc %{_texmfdistdir}/doc/latex/zxjatype/example/example.pdf
%doc %{_texmfdistdir}/doc/latex/zxjatype/example/example.tex
%doc %{_texmfdistdir}/doc/latex/zxjatype/example/xetexsamp01.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
