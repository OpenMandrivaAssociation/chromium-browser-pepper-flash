%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:        Chromium Flash player plugin
Name:           chromium-browser-pepper-flash
Version:        15.0.0.152
Release:        1

License:        Proprietary
Url:            http://www.google.com/chrome
Group:          Networking/WWW
Source0:        https://dl.google.com/linux/direct/google-chrome-stable_current_i386.rpm
Source1:        https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm

BuildRequires:  rpm cpio

Requires:       chromium-browser

%description
Pepper API based Adobe Flash plugin for Google's Open Source browser Chromium.

%package -n chromium-browser-pdf-plugin
Summary:        Chromium PDF viewer plugin
Group:          Networking/WWW
Requires:       chromium-browser

%description -n chromium-browser-pdf-plugin
Official PDF viewer plugin for Google's Open Source browser Chromium.

%prep
%setup -c -T


%build
%ifarch x86_64
rpm2cpio %{SOURCE1} | cpio -idmv
%else
rpm2cpio %{SOURCE0} | cpio -idmv
%endif


%install
mkdir -p %{buildroot}%{_libdir}/chromium-browser/PepperFlash/
install -m644 opt/google/chrome/PepperFlash/* %{buildroot}%{_libdir}/chromium-browser/PepperFlash/ 
install -m755 opt/google/chrome/libpdf.so %{buildroot}%{_libdir}/chromium-browser/


%files
%dir %{_libdir}/chromium-browser/
%{_libdir}/chromium-browser/PepperFlash/


%files -n chromium-browser-pdf-plugin
%{_libdir}/chromium-browser/libpdf.so

