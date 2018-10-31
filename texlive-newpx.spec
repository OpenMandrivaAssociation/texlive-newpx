Name:		texlive-newpx
Version:	1.321
Release:	2
Summary:	Alternative uses of the PX fonts, with improved metrics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/newpx
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newpx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newpx.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package, based on pxfonts, provides many fixes and
enhancements to that package, and splits it in two parts
(newpxtext and newpxmath) which may be run independently of one
another. It provides scaling, improved metrics, and other
options. For proper operation, the packages require that the
packages newtxmath and txfonts be installed and their map files
enabled.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/newpx
%{_texmfdistdir}/fonts/map/dvips/newpx
%{_texmfdistdir}/fonts/afm/public/newpx
%{_texmfdistdir}/fonts/tfm/public/newpx
%{_texmfdistdir}/fonts/opentype/public/newpx
%{_texmfdistdir}/fonts/type1/public/newpx
%{_texmfdistdir}/fonts/vf/public/newpx
%{_texmfdistdir}/tex/latex/newpx
%doc %{_texmfdistdir}/doc/fonts/newpx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
