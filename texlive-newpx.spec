# revision 33379
# category Package
# catalog-ctan /fonts/newpx
# catalog-date 2014-04-05 09:51:45 +0200
# catalog-license lppl
# catalog-version 1.122
Name:		texlive-newpx
Version:	1.122
Release:	1
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
%{_texmfdistdir}/fonts/enc/dvips/newpx/a_3p3as7.enc
%{_texmfdistdir}/fonts/enc/dvips/newpx/a_4dmj3j.enc
%{_texmfdistdir}/fonts/enc/dvips/newpx/a_6lauhs.enc
%{_texmfdistdir}/fonts/enc/dvips/newpx/a_6vkyws.enc
%{_texmfdistdir}/fonts/enc/dvips/newpx/a_amdua2.enc
%{_texmfdistdir}/fonts/enc/dvips/newpx/a_apar7h.enc
%{_texmfdistdir}/fonts/enc/dvips/newpx/a_cbygv3.enc
%{_texmfdistdir}/fonts/enc/dvips/newpx/a_djwvt2.enc
%{_texmfdistdir}/fonts/enc/dvips/newpx/a_dmxceb.enc
%{_texmfdistdir}/fonts/enc/dvips/newpx/a_dp6dg4.enc
%{_texmfdistdir}/fonts/enc/dvips/newpx/a_fenm72.enc
%{_texmfdistdir}/fonts/enc/dvips/newpx/a_gmpqcc.enc
%{_texmfdistdir}/fonts/enc/dvips/newpx/a_hokgb6.enc
%{_texmfdistdir}/fonts/enc/dvips/newpx/a_k3mk5v.enc
%{_texmfdistdir}/fonts/enc/dvips/newpx/a_m53eq4.enc
%{_texmfdistdir}/fonts/enc/dvips/newpx/a_ncu7e3.enc
%{_texmfdistdir}/fonts/enc/dvips/newpx/a_nfmpiy.enc
%{_texmfdistdir}/fonts/enc/dvips/newpx/a_nyan3h.enc
%{_texmfdistdir}/fonts/enc/dvips/newpx/a_oi5fc3.enc
%{_texmfdistdir}/fonts/enc/dvips/newpx/a_otqgcp.enc
%{_texmfdistdir}/fonts/enc/dvips/newpx/a_pqtwkv.enc
%{_texmfdistdir}/fonts/enc/dvips/newpx/a_rg6izg.enc
%{_texmfdistdir}/fonts/enc/dvips/newpx/a_tkkaeb.enc
%{_texmfdistdir}/fonts/enc/dvips/newpx/a_u7du6i.enc
%{_texmfdistdir}/fonts/enc/dvips/newpx/a_uv5sju.enc
%{_texmfdistdir}/fonts/enc/dvips/newpx/a_yi34h6.enc
%{_texmfdistdir}/fonts/enc/dvips/newpx/a_zomyng.enc
%{_texmfdistdir}/fonts/enc/dvips/newpx/tgpdiff.enc
%{_texmfdistdir}/fonts/map/dvips/newpx/newpx.map
%{_texmfdistdir}/fonts/tfm/public/newpx/LY1-TeXGyrePagellaX-Bold-lnum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/LY1-TeXGyrePagellaX-Bold-lnum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/LY1-TeXGyrePagellaX-Bold-onum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/LY1-TeXGyrePagellaX-Bold-onum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/LY1-TeXGyrePagellaX-Bold-pnum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/LY1-TeXGyrePagellaX-Bold-pnum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/LY1-TeXGyrePagellaX-BoldItalic-lnum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/LY1-TeXGyrePagellaX-BoldItalic-lnum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/LY1-TeXGyrePagellaX-BoldItalic-onum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/LY1-TeXGyrePagellaX-BoldItalic-onum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/LY1-TeXGyrePagellaX-BoldItalic-pnum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/LY1-TeXGyrePagellaX-BoldItalic-pnum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/LY1-TeXGyrePagellaX-Italic-lnum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/LY1-TeXGyrePagellaX-Italic-lnum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/LY1-TeXGyrePagellaX-Italic-onum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/LY1-TeXGyrePagellaX-Italic-onum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/LY1-TeXGyrePagellaX-Italic-pnum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/LY1-TeXGyrePagellaX-Italic-pnum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/LY1-TeXGyrePagellaX-Regular-lnum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/LY1-TeXGyrePagellaX-Regular-lnum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/LY1-TeXGyrePagellaX-Regular-onum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/LY1-TeXGyrePagellaX-Regular-onum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/LY1-TeXGyrePagellaX-Regular-pnum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/LY1-TeXGyrePagellaX-Regular-pnum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/LY1-TeXGyrePagellaX-Regular-sups-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/LY1-TeXGyrePagellaX-Regular-sups-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/OT1-TeXGyrePagellaX-Bold-lnum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/OT1-TeXGyrePagellaX-Bold-lnum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/OT1-TeXGyrePagellaX-Bold-onum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/OT1-TeXGyrePagellaX-Bold-onum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/OT1-TeXGyrePagellaX-Bold-pnum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/OT1-TeXGyrePagellaX-Bold-pnum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/OT1-TeXGyrePagellaX-BoldItalic-lnum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/OT1-TeXGyrePagellaX-BoldItalic-lnum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/OT1-TeXGyrePagellaX-BoldItalic-onum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/OT1-TeXGyrePagellaX-BoldItalic-onum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/OT1-TeXGyrePagellaX-BoldItalic-pnum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/OT1-TeXGyrePagellaX-BoldItalic-pnum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/OT1-TeXGyrePagellaX-Italic-lnum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/OT1-TeXGyrePagellaX-Italic-lnum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/OT1-TeXGyrePagellaX-Italic-onum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/OT1-TeXGyrePagellaX-Italic-onum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/OT1-TeXGyrePagellaX-Italic-pnum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/OT1-TeXGyrePagellaX-Italic-pnum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/OT1-TeXGyrePagellaX-Regular-lnum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/OT1-TeXGyrePagellaX-Regular-lnum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/OT1-TeXGyrePagellaX-Regular-onum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/OT1-TeXGyrePagellaX-Regular-onum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/OT1-TeXGyrePagellaX-Regular-pnum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/OT1-TeXGyrePagellaX-Regular-pnum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/OT1-TeXGyrePagellaX-Regular-sups-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/OT1-TeXGyrePagellaX-Regular-sups-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Bold-lnum-kern-liga--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Bold-lnum-kern-liga-smcp--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Bold-lnum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Bold-lnum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Bold-onum-kern-liga--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Bold-onum-kern-liga-smcp--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Bold-onum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Bold-onum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Bold-pnum-kern-liga--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Bold-pnum-kern-liga-smcp--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Bold-pnum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Bold-pnum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-BoldItalic-lnum-kern-liga--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-BoldItalic-lnum-kern-liga-smcp--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-BoldItalic-lnum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-BoldItalic-lnum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-BoldItalic-onum-kern-liga--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-BoldItalic-onum-kern-liga-smcp--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-BoldItalic-onum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-BoldItalic-onum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-BoldItalic-pnum-kern-liga--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-BoldItalic-pnum-kern-liga-smcp--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-BoldItalic-pnum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-BoldItalic-pnum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Italic-lnum-kern-liga--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Italic-lnum-kern-liga-smcp--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Italic-lnum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Italic-lnum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Italic-onum-kern-liga--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Italic-onum-kern-liga-smcp--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Italic-onum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Italic-onum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Italic-pnum-kern-liga--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Italic-pnum-kern-liga-smcp--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Italic-pnum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Italic-pnum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Regular-lnum-kern-liga--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Regular-lnum-kern-liga-smcp--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Regular-lnum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Regular-lnum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Regular-onum-kern-liga--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Regular-onum-kern-liga-smcp--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Regular-onum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Regular-onum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Regular-pnum-kern-liga--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Regular-pnum-kern-liga-smcp--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Regular-pnum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Regular-pnum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Regular-sups-kern-liga--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Regular-sups-kern-liga-smcp--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Regular-sups-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/T1-TeXGyrePagellaX-Regular-sups-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Bold-lnum-kern-liga--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Bold-lnum-kern-liga-smcp--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Bold-lnum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Bold-lnum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Bold-onum-kern-liga--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Bold-onum-kern-liga-smcp--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Bold-onum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Bold-onum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Bold-pnum-kern-liga--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Bold-pnum-kern-liga-smcp--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Bold-pnum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Bold-pnum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-BoldItalic-lnum-kern-liga--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-BoldItalic-lnum-kern-liga-smcp--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-BoldItalic-lnum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-BoldItalic-lnum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-BoldItalic-onum-kern-liga--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-BoldItalic-onum-kern-liga-smcp--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-BoldItalic-onum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-BoldItalic-onum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-BoldItalic-pnum-kern-liga--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-BoldItalic-pnum-kern-liga-smcp--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-BoldItalic-pnum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-BoldItalic-pnum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Italic-lnum-kern-liga--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Italic-lnum-kern-liga-smcp--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Italic-lnum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Italic-lnum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Italic-onum-kern-liga--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Italic-onum-kern-liga-smcp--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Italic-onum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Italic-onum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Italic-pnum-kern-liga--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Italic-pnum-kern-liga-smcp--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Italic-pnum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Italic-pnum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Regular-lnum-kern-liga--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Regular-lnum-kern-liga-smcp--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Regular-lnum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Regular-lnum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Regular-onum-kern-liga--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Regular-onum-kern-liga-smcp--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Regular-onum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Regular-onum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Regular-pnum-kern-liga--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Regular-pnum-kern-liga-smcp--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Regular-pnum-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Regular-pnum-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Regular-sups-kern-liga--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Regular-sups-kern-liga-smcp--base.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Regular-sups-kern-liga-smcp.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/TS1-TeXGyrePagellaX-Regular-sups-kern-liga.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/zplb-x.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/zplbexa.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/zplbexx.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/zplbmi.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/zplbmi1.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/zplbmia.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/zplbsy.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/zplbsya.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/zplbsyb.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/zplbsyc.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/zplexa.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/zplexx.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/zplmi.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/zplmi1.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/zplmia.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/zplr-x.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/zplsy.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/zplsya.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/zplsyb.tfm
%{_texmfdistdir}/fonts/tfm/public/newpx/zplsyc.tfm
%{_texmfdistdir}/fonts/type1/public/newpx/TeXGyrePagellaX-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/newpx/TeXGyrePagellaX-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/public/newpx/TeXGyrePagellaX-Italic.pfb
%{_texmfdistdir}/fonts/type1/public/newpx/TeXGyrePagellaX-Regular.pfb
%{_texmfdistdir}/fonts/type1/public/newpx/zplx-bold.pfb
%{_texmfdistdir}/fonts/type1/public/newpx/zplx-regular.pfb
%{_texmfdistdir}/fonts/vf/public/newpx/T1-TeXGyrePagellaX-Bold-lnum-kern-liga-smcp.vf
%{_texmfdistdir}/fonts/vf/public/newpx/T1-TeXGyrePagellaX-Bold-lnum-kern-liga.vf
%{_texmfdistdir}/fonts/vf/public/newpx/T1-TeXGyrePagellaX-Bold-onum-kern-liga-smcp.vf
%{_texmfdistdir}/fonts/vf/public/newpx/T1-TeXGyrePagellaX-Bold-onum-kern-liga.vf
%{_texmfdistdir}/fonts/vf/public/newpx/T1-TeXGyrePagellaX-Bold-pnum-kern-liga-smcp.vf
%{_texmfdistdir}/fonts/vf/public/newpx/T1-TeXGyrePagellaX-Bold-pnum-kern-liga.vf
%{_texmfdistdir}/fonts/vf/public/newpx/T1-TeXGyrePagellaX-BoldItalic-lnum-kern-liga-smcp.vf
%{_texmfdistdir}/fonts/vf/public/newpx/T1-TeXGyrePagellaX-BoldItalic-lnum-kern-liga.vf
%{_texmfdistdir}/fonts/vf/public/newpx/T1-TeXGyrePagellaX-BoldItalic-onum-kern-liga-smcp.vf
%{_texmfdistdir}/fonts/vf/public/newpx/T1-TeXGyrePagellaX-BoldItalic-onum-kern-liga.vf
%{_texmfdistdir}/fonts/vf/public/newpx/T1-TeXGyrePagellaX-BoldItalic-pnum-kern-liga-smcp.vf
%{_texmfdistdir}/fonts/vf/public/newpx/T1-TeXGyrePagellaX-BoldItalic-pnum-kern-liga.vf
%{_texmfdistdir}/fonts/vf/public/newpx/T1-TeXGyrePagellaX-Italic-lnum-kern-liga-smcp.vf
%{_texmfdistdir}/fonts/vf/public/newpx/T1-TeXGyrePagellaX-Italic-lnum-kern-liga.vf
%{_texmfdistdir}/fonts/vf/public/newpx/T1-TeXGyrePagellaX-Italic-onum-kern-liga-smcp.vf
%{_texmfdistdir}/fonts/vf/public/newpx/T1-TeXGyrePagellaX-Italic-onum-kern-liga.vf
%{_texmfdistdir}/fonts/vf/public/newpx/T1-TeXGyrePagellaX-Italic-pnum-kern-liga-smcp.vf
%{_texmfdistdir}/fonts/vf/public/newpx/T1-TeXGyrePagellaX-Italic-pnum-kern-liga.vf
%{_texmfdistdir}/fonts/vf/public/newpx/T1-TeXGyrePagellaX-Regular-lnum-kern-liga-smcp.vf
%{_texmfdistdir}/fonts/vf/public/newpx/T1-TeXGyrePagellaX-Regular-lnum-kern-liga.vf
%{_texmfdistdir}/fonts/vf/public/newpx/T1-TeXGyrePagellaX-Regular-onum-kern-liga-smcp.vf
%{_texmfdistdir}/fonts/vf/public/newpx/T1-TeXGyrePagellaX-Regular-onum-kern-liga.vf
%{_texmfdistdir}/fonts/vf/public/newpx/T1-TeXGyrePagellaX-Regular-pnum-kern-liga-smcp.vf
%{_texmfdistdir}/fonts/vf/public/newpx/T1-TeXGyrePagellaX-Regular-pnum-kern-liga.vf
%{_texmfdistdir}/fonts/vf/public/newpx/T1-TeXGyrePagellaX-Regular-sups-kern-liga-smcp.vf
%{_texmfdistdir}/fonts/vf/public/newpx/T1-TeXGyrePagellaX-Regular-sups-kern-liga.vf
%{_texmfdistdir}/fonts/vf/public/newpx/TS1-TeXGyrePagellaX-Bold-lnum-kern-liga-smcp.vf
%{_texmfdistdir}/fonts/vf/public/newpx/TS1-TeXGyrePagellaX-Bold-lnum-kern-liga.vf
%{_texmfdistdir}/fonts/vf/public/newpx/TS1-TeXGyrePagellaX-Bold-onum-kern-liga-smcp.vf
%{_texmfdistdir}/fonts/vf/public/newpx/TS1-TeXGyrePagellaX-Bold-onum-kern-liga.vf
%{_texmfdistdir}/fonts/vf/public/newpx/TS1-TeXGyrePagellaX-Bold-pnum-kern-liga-smcp.vf
%{_texmfdistdir}/fonts/vf/public/newpx/TS1-TeXGyrePagellaX-Bold-pnum-kern-liga.vf
%{_texmfdistdir}/fonts/vf/public/newpx/TS1-TeXGyrePagellaX-BoldItalic-lnum-kern-liga-smcp.vf
%{_texmfdistdir}/fonts/vf/public/newpx/TS1-TeXGyrePagellaX-BoldItalic-lnum-kern-liga.vf
%{_texmfdistdir}/fonts/vf/public/newpx/TS1-TeXGyrePagellaX-BoldItalic-onum-kern-liga-smcp.vf
%{_texmfdistdir}/fonts/vf/public/newpx/TS1-TeXGyrePagellaX-BoldItalic-onum-kern-liga.vf
%{_texmfdistdir}/fonts/vf/public/newpx/TS1-TeXGyrePagellaX-BoldItalic-pnum-kern-liga-smcp.vf
%{_texmfdistdir}/fonts/vf/public/newpx/TS1-TeXGyrePagellaX-BoldItalic-pnum-kern-liga.vf
%{_texmfdistdir}/fonts/vf/public/newpx/TS1-TeXGyrePagellaX-Italic-lnum-kern-liga-smcp.vf
%{_texmfdistdir}/fonts/vf/public/newpx/TS1-TeXGyrePagellaX-Italic-lnum-kern-liga.vf
%{_texmfdistdir}/fonts/vf/public/newpx/TS1-TeXGyrePagellaX-Italic-onum-kern-liga-smcp.vf
%{_texmfdistdir}/fonts/vf/public/newpx/TS1-TeXGyrePagellaX-Italic-onum-kern-liga.vf
%{_texmfdistdir}/fonts/vf/public/newpx/TS1-TeXGyrePagellaX-Italic-pnum-kern-liga-smcp.vf
%{_texmfdistdir}/fonts/vf/public/newpx/TS1-TeXGyrePagellaX-Italic-pnum-kern-liga.vf
%{_texmfdistdir}/fonts/vf/public/newpx/TS1-TeXGyrePagellaX-Regular-lnum-kern-liga-smcp.vf
%{_texmfdistdir}/fonts/vf/public/newpx/TS1-TeXGyrePagellaX-Regular-lnum-kern-liga.vf
%{_texmfdistdir}/fonts/vf/public/newpx/TS1-TeXGyrePagellaX-Regular-onum-kern-liga-smcp.vf
%{_texmfdistdir}/fonts/vf/public/newpx/TS1-TeXGyrePagellaX-Regular-onum-kern-liga.vf
%{_texmfdistdir}/fonts/vf/public/newpx/TS1-TeXGyrePagellaX-Regular-pnum-kern-liga-smcp.vf
%{_texmfdistdir}/fonts/vf/public/newpx/TS1-TeXGyrePagellaX-Regular-pnum-kern-liga.vf
%{_texmfdistdir}/fonts/vf/public/newpx/TS1-TeXGyrePagellaX-Regular-sups-kern-liga-smcp.vf
%{_texmfdistdir}/fonts/vf/public/newpx/TS1-TeXGyrePagellaX-Regular-sups-kern-liga.vf
%{_texmfdistdir}/fonts/vf/public/newpx/zplbexa.vf
%{_texmfdistdir}/fonts/vf/public/newpx/zplbexx.vf
%{_texmfdistdir}/fonts/vf/public/newpx/zplbmi.vf
%{_texmfdistdir}/fonts/vf/public/newpx/zplbmi1.vf
%{_texmfdistdir}/fonts/vf/public/newpx/zplbmia.vf
%{_texmfdistdir}/fonts/vf/public/newpx/zplbsy.vf
%{_texmfdistdir}/fonts/vf/public/newpx/zplbsya.vf
%{_texmfdistdir}/fonts/vf/public/newpx/zplbsyb.vf
%{_texmfdistdir}/fonts/vf/public/newpx/zplbsyc.vf
%{_texmfdistdir}/fonts/vf/public/newpx/zplexa.vf
%{_texmfdistdir}/fonts/vf/public/newpx/zplexx.vf
%{_texmfdistdir}/fonts/vf/public/newpx/zplmi.vf
%{_texmfdistdir}/fonts/vf/public/newpx/zplmi1.vf
%{_texmfdistdir}/fonts/vf/public/newpx/zplmia.vf
%{_texmfdistdir}/fonts/vf/public/newpx/zplsy.vf
%{_texmfdistdir}/fonts/vf/public/newpx/zplsya.vf
%{_texmfdistdir}/fonts/vf/public/newpx/zplsyb.vf
%{_texmfdistdir}/fonts/vf/public/newpx/zplsyc.vf
%{_texmfdistdir}/tex/latex/newpx/ly1npxss.fd
%{_texmfdistdir}/tex/latex/newpx/ly1npxtt.fd
%{_texmfdistdir}/tex/latex/newpx/ly1zpl1.fd
%{_texmfdistdir}/tex/latex/newpx/ly1zpl2.fd
%{_texmfdistdir}/tex/latex/newpx/ly1zplj.fd
%{_texmfdistdir}/tex/latex/newpx/ly1zplx.fd
%{_texmfdistdir}/tex/latex/newpx/newpxmath.sty
%{_texmfdistdir}/tex/latex/newpx/newpxtext.sty
%{_texmfdistdir}/tex/latex/newpx/omlnpxmi.fd
%{_texmfdistdir}/tex/latex/newpx/omsnpxsy.fd
%{_texmfdistdir}/tex/latex/newpx/ot1npxss.fd
%{_texmfdistdir}/tex/latex/newpx/ot1npxtt.fd
%{_texmfdistdir}/tex/latex/newpx/ot1zpl1.fd
%{_texmfdistdir}/tex/latex/newpx/ot1zpl2.fd
%{_texmfdistdir}/tex/latex/newpx/ot1zplj.fd
%{_texmfdistdir}/tex/latex/newpx/ot1zplx.fd
%{_texmfdistdir}/tex/latex/newpx/t1npxss.fd
%{_texmfdistdir}/tex/latex/newpx/t1npxtt.fd
%{_texmfdistdir}/tex/latex/newpx/t1zpl1.fd
%{_texmfdistdir}/tex/latex/newpx/t1zpl2.fd
%{_texmfdistdir}/tex/latex/newpx/t1zplj.fd
%{_texmfdistdir}/tex/latex/newpx/t1zplx.fd
%{_texmfdistdir}/tex/latex/newpx/ts1npxss.fd
%{_texmfdistdir}/tex/latex/newpx/ts1npxtt.fd
%{_texmfdistdir}/tex/latex/newpx/ts1zpl1.fd
%{_texmfdistdir}/tex/latex/newpx/ts1zpl2.fd
%{_texmfdistdir}/tex/latex/newpx/ts1zplj.fd
%{_texmfdistdir}/tex/latex/newpx/ts1zplx.fd
%{_texmfdistdir}/tex/latex/newpx/unpxexa.fd
%{_texmfdistdir}/tex/latex/newpx/unpxmia.fd
%{_texmfdistdir}/tex/latex/newpx/unpxss.fd
%{_texmfdistdir}/tex/latex/newpx/unpxsya.fd
%{_texmfdistdir}/tex/latex/newpx/unpxsyb.fd
%{_texmfdistdir}/tex/latex/newpx/unpxsyc.fd
%{_texmfdistdir}/tex/latex/newpx/unpxtt.fd
%doc %{_texmfdistdir}/doc/fonts/newpx/MANIFEST-newpx.txt
%doc %{_texmfdistdir}/doc/fonts/newpx/README
%doc %{_texmfdistdir}/doc/fonts/newpx/newpxdoc.pdf
%doc %{_texmfdistdir}/doc/fonts/newpx/newpxdoc.tex
%doc %{_texmfdistdir}/doc/fonts/newpx/newpxeg-crop.pdf
%doc %{_texmfdistdir}/doc/fonts/newpx/pxfontseg-crop.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
