%global tl_name newpx
%global tl_revision 79618
%global tl_version 1.551

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Alternative uses of the PX fonts, with improved metrics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/newpx
License:	lppl1.3 gfl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newpx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newpx.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newpx.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
This package, initially based on pxfonts, provides many fixes and
enhancements to that package, and splits it in two parts (newpxtext and
newpxmath) which may be run independently of one another. It provides
scaling, improved metrics, and other options. For proper operation, the
packages require that the packages newtxmath, pxfonts, and
TeXGyrePagella be installed and their map files enabled.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from newpx:
Map newpx.map
TL_DROPIN_EOF
