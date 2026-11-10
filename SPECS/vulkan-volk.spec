%global debug_package %{nil}

Name:           vulkan-volk
Version:        1.4.341.0
Release:        1%{?dist}
Summary:        Meta loader for Vulkan API

License:        MIT
URL:            https://github.com/zeux/volk
Source0:        %url/archive/vulkan-sdk-%{version}.tar.gz#/Vulkan-Volk-sdk-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  vulkan-headers

%description
%{summary}

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}
Requires:       vulkan-headers
Conflicts:      volk-devel

%description    devel
%{summary}

%prep
%autosetup -n volk-vulkan-sdk-%{version} -p1

%build
%cmake -DCMAKE_BUILD_TYPE=Release \
       -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
       -DVOLK_INSTALL:BOOL=ON
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE.md
%doc README.md
%dir %{_libdir}/cmake/volk
%{_includedir}/volk.h
%{_includedir}/volk.c
%{_libdir}/cmake/volk/*.cmake
%{_libdir}/libvolk.a

%changelog
* Thu May 21 2026 Anusha Srivatsa <asrivats@redhat.com> - 1.4.341.0-1
- Update to 1.4.341.0 SDK

* Wed 07 2026 José Expósito <jexposit@redhat.com> - 1.4.328.1-1
- Update to 1.4.328.1 SDK

* Thu Jun 26 2025 Anusha Srivatsa <asrivats@redhat.com> - 1.4.313.0-1
- Update to 1.4.313.0 SDK

* Mon Jan 20 2025 José Expósito <jexposit@redhat.com> - 1.4.304.0-1
- Update to 1.4.304.0 SDK

* Thu Jan 11 2024 José Expósito <jexposit@redhat.com> - 1.3.270-1
- Version 1.3.270
