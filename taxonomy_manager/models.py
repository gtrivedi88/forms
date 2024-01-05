        # Add Product Mkt Life
        product_mkt_life = ProductMktLife(
            product_id=new_product.product_id,
            product_release=form.product_release.data,
            product_release_detail=form.product_release_detail.data,
            product_release_link=form.product_release_link.data,
            product_eol=form.product_eol.data,
            product_eol_detail=form.product_eol_detail.data,
            product_eol_link=form.product_eol_link.data
        )
        db.session.add(product_mkt_life)
