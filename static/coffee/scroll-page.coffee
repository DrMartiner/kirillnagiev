$(document).ready () ->
    scrollBlock = $('#' + scrollBlockId)

    if scrollBlock.length
        if scrollBlock[0].scrollHeight > scrollBlock.height()
            $('.arrow').removeClass 'hide-arrow'

            $('.arrow.up').mousedown () ->
                if scrollBlock.scrollTop() + scrollBlock.outerHeight() <= scrollBlock.height()
                    return

                scrollBlock.animate {scrollTop: 0}, scrollPageSpeed, () ->

            $('.arrow.down').mousedown () ->
                if scrollBlock.scrollTop() + scrollBlock.outerHeight() >= scrollBlock[0].scrollHeight
                    return

                scrollBlock.animate {scrollTop: scrollBlock[0].scrollHeight}, scrollPageSpeed, () ->