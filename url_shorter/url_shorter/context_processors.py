def currentPage(request):
    if request.resolver_match:
        return {
            "current_app": request.resolver_match.app_name,
            # "current_view": request.resolver_match.url_name,
        }

    return {
        "current_app": "",
        # "current_view": "",
    }