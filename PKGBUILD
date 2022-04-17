# Maintainer: Michael John <amstelchen at gmail dot com>

pkgname=primegridparser
_pkgname=PrimeGridParser
pkgver=0.1.0
pkgrel=1
pkgdesc="Show a PrimeGrid user's badges."
arch=('any')
url="http://github.com/amstelchen/PrimeGridParser"
license=('GPL')
packager=('Michael John')
depends=('python' 'python-pandas' 'python-beautifulsoup4')
optdepends=('')
makedepends=(python-build python-installer)
source=("${pkgname}_${pkgver}.tar.gz"::"https://github.com/amstelchen/PrimeGridParser/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('833432a0284fe874e082d4cb2f0639d106b8c527b1a408c2caec2f22b3cb9558')

#build() {
#    python -m build --wheel --no-isolation
#}

package() {
    #python -m installer --destdir="$pkgdir" dist/*.whl

  install -Dm755 "${srcdir}/${_pkgname}-${pkgver}"/PrimeGridParser.py \
      "${pkgdir}"/usr/bin/PrimeGridParser
}
