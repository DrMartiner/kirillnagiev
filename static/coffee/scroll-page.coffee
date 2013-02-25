$(document).ready () ->
    scrollBlock = $('#' + scrollBlockId)

    if scrollBlock.length
        if scrollBlock[0].scrollHeight > scrollBlock.height()
            enableBtns = () ->
                $('.arrow').removeAttr 'disabled'

            disableBtns = () ->
                $('.arrow').attr 'disabled', 'disabled'

            $('.arrow').removeClass 'hide-arrow'

            $('.arrow.up').mousedown () ->
                if scrollBlock.scrollTop() + scrollBlock.outerHeight() <= scrollBlock.height() || $('.arrow').attr 'disabled'
                    return

                disableBtns()
                scrollTo = scrollBlock.scrollTop() - parseInt(scrollBlock.outerHeight() * scrollSizePercent)
                scrollBlock.animate {scrollTop: scrollTo}, scrollPageSpeed, () ->
                    enableBtns()

            $('.arrow.down').mousedown () ->

                if scrollBlock.scrollTop() + scrollBlock.outerHeight() >= scrollBlock[0].scrollHeight || $(this).attr 'disabled'
                    return

                disableBtns()
                scrollTo = scrollBlock.scrollTop() + parseInt(scrollBlock.outerHeight() * scrollSizePercent)
                scrollBlock.animate {scrollTop: scrollTo}, scrollPageSpeed, () ->
                    enableBtns()