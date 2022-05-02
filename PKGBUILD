# Maintainer: Michael John <amstelchen at gmail dot com>

pkgname=primegridparser
_pkgname=PrimeGridParser
pkgver=0.2.0
pkgrel=1
pkgdesc="Show a PrimeGrid user's badges."
arch=('any')
url="http://github.com/amstelchen/PrimeGridParser"
license=('GPL')
packager=('Michael John')
depends=('python' 'python-beautifulsoup4' 'python-prettytable' 'python-requests' 'python-argparse')
optdepends=('')
makedepends=(python-build python-installer)
source=("${pkgname}_${pkgver}.tar.gz"::"https://github.com/amstelchen/PrimeGridParser/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('c69b5985fbd8aebbe7bad33b22da2c46b3fb1ccf11c8e12164de3b2b8d492003')

build() {
    #python -m build --wheel --no-isolation
    cd "${srcdir}/${_pkgname}-${pkgver}"
    poetry build
}

package() {
    #python -m installer --destdir="$pkgdir" dist/*.whl
    pip install "${srcdir}/${_pkgname}-${pkgver}"

    install -Dm755 "${srcdir}/${_pkgname}-${pkgver}/${pkgname}"/__main__.py \
      "${pkgdir}"/usr/bin/PrimeGridParser
}
