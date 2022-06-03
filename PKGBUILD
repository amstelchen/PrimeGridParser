# Maintainer: Michael John <amstelchen at gmail dot com>

pkgname=primegridparser
_pkgname=PrimeGridParser
pkgver=0.3.0
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
#source=("${pkgname}_${pkgver}.tar.gz"::"https://github.com/amstelchen/PrimeGridParser/raw/master/dist/primegridparser-0.2.0-py3-none-any.whl")
sha256sums=('fc4b679683d6eee262a4cc03a692e80f773e2a7c1626ae053dc7968e85888c23')

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
