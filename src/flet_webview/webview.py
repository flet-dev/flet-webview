import asyncio
from typing import Optional

import flet as ft

from .types import (
    RequestMethod,
    WebViewConsoleMessageEvent,
    WebViewJavaScriptEvent,
    WebViewScrollEvent,
)

__all__ = ["WebView"]


@ft.control("WebView")
class WebView(ft.ConstrainedControl):
    """
    Easily load webpages while allowing user interaction.

    Note:
        Works only on the following platforms: iOS, Android, macOS and Web.
    """

    url: str
    """The URL of the web page to load."""

    enable_javascript: Optional[bool] = None
    """
    Enable or disable the JavaScript execution on the page.

    Note that disabling the JavaScript execution on the page may result to
    unexpected web page behaviour.
    """

    prevent_links: Optional[list[str]] = None
    """List of url-prefixes that should not be followed/loaded/downloaded."""

    bgcolor: Optional[ft.ColorValue] = None
    """Defines the background color of the WebView."""

    on_page_started: Optional[ft.ControlEventHandler["WebView"]] = None
    """
    Fires soon as the first loading process of the webview page is started.

    Event handler argument's [`data`][flet.Event.data] property is of type
    `str` and contains the URL.

    Note:
        Works only on the following platforms: iOS, Android and macOS.
    """

    on_page_ended: Optional[ft.ControlEventHandler["WebView"]] = None
    """
    Fires when all the webview page loading processes are ended.

    Event handler argument's [`data`][flet.Event.data] property is of type `str`
    and contains the URL.

    Note:
        Works only on the following platforms: iOS, Android and macOS.
    """

    on_web_resource_error: Optional[ft.ControlEventHandler["WebView"]] = None
    """
    Fires when there is error with loading a webview page resource.

    Event handler argument's [`data`][flet.Event.data] property is of type
    `str` and contains the error message.

    Note:
        Works only on the following platforms: iOS, Android and macOS.
    """

    on_progress: Optional[ft.ControlEventHandler["WebView"]] = None
    """
    Fires when the progress of the webview page loading is changed.

    Event handler argument's [`data`][flet.Event.data] property is of type
    `int` and contains the progress value.

    Note:
        Works only on the following platforms: iOS, Android and macOS.
    """

    on_url_change: Optional[ft.ControlEventHandler["WebView"]] = None
    """
    Fires when the URL of the webview page is changed.

    Event handler argument's [`data`][flet.Event.data] property is of type
    `str` and contains the new URL.

    Note:
        Works only on the following platforms: iOS, Android and macOS.
    """

    on_scroll: Optional[ft.EventHandler[WebViewScrollEvent]] = None
    """
    Fires when the web page's scroll position changes.

    Note:
        Works only on the following platforms: iOS, Android and macOS.
    """

    on_console_message: Optional[ft.EventHandler[WebViewConsoleMessageEvent]] = None
    """
    Fires when a log message is written to the JavaScript console.

    Note:
        Works only on the following platforms: iOS, Android and macOS.
    """

    on_javascript_alert_dialog: Optional[ft.EventHandler[WebViewJavaScriptEvent]] = None
    """
    Fires when the web page attempts to display a JavaScript alert() dialog.

    Note:
        Works only on the following platforms: iOS, Android and macOS.
    """

    def _check_mobile_or_mac_platform(self):
        """
        Checks/Validates support for the current platform (iOS, Android, or macOS).
        """
        assert self.page is not None, "WebView must be added to page first."
        if self.page.web or self.page.platform not in [
            ft.PagePlatform.ANDROID,
            ft.PagePlatform.IOS,
            ft.PagePlatform.MACOS,
        ]:
            raise ft.FletUnsupportedPlatformException(
                "This method is supported on Android, iOS and macOS platforms only."
            )

    def reload(self):
        """
        Reloads the current URL.

        Note:
            Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.reload_async())

    async def reload_async(self):
        """
        Reloads the current URL.

        Note:
            Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async("reload")

    async def can_go_back_async(self) -> bool:
        """
        Whether there's a back history item.

        Returns:
            `True` if there is a back history item, `False` otherwise.

        Note:
            Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        return await self._invoke_method_async("can_go_back")

    async def can_go_forward(self) -> bool:
        """
        Whether there's a forward history item.

        Returns:
            `True` if there is a forward history item, `False` otherwise.

        Note:
            Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        return await self._invoke_method_async("can_go_forward")

    def go_back(self):
        """
        Go back in the history of the webview, if `can_go_back()` is `True`.

        Note:
            Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.go_back_async())

    async def go_back_async(self):
        """
        Go back in the history of the webview, if `can_go_back()` is `True`.

        Note:
            Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async("go_back")

    def go_forward(self):
        """
        Go forward in the history of the webview, if `can_go_forward()` is `True`.

        Note:
            Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.go_forward_async())

    async def go_forward_async(self):
        """
        Go forward in the history of the webview, if `can_go_forward()` is `True`.

        Note:
            Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async("go_forward")

    def enable_zoom(self):
        """
        Enable zooming using the on-screen zoom controls and gestures.

        Note:
            Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.enable_zoom_async())

    async def enable_zoom_async(self):
        """
        Enable zooming using the on-screen zoom controls and gestures.

        Note:
            Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async("enable_zoom")

    def disable_zoom(self):
        """
        Disable zooming using the on-screen zoom controls and gestures.

        Note:
            Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.disable_zoom_async())

    async def disable_zoom_async(self):
        """
        Disable zooming using the on-screen zoom controls and gestures.

        Note:
            Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async("disable_zoom")

    def clear_cache(self):
        """
        Clears all caches used by the WebView.

        The following caches are cleared:
            - Browser HTTP Cache
            - Cache API caches. Service workers tend to use this cache.
            - Application cache

        Note:
            Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.clear_cache_async())

    async def clear_cache_async(self):
        """
        Clears all caches used by the WebView.

        The following caches are cleared:
            - Browser HTTP Cache
            - Cache API caches. Service workers tend to use this cache.
            - Application cache

        Note:
            Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async("clear_cache")

    def clear_local_storage(self):
        """
        Clears the local storage used by the WebView.

        Note:
            Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.clear_local_storage_async())

    async def clear_local_storage_async(self):
        """
        Clears the local storage used by the WebView.

        Note:
            Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async("clear_local_storage")

    async def get_current_url_async(self) -> Optional[str]:
        """
        Returns the current URL that the WebView is displaying or `None`
        if no URL was ever loaded.

        Returns:
            The current URL that the WebView is displaying or `None`
            if no URL was ever loaded.

        Note:
            Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        return await self._invoke_method_async("get_current_url")

    async def get_title_async(self) -> Optional[str]:
        """
        Returns the title of the currently loaded page.

        Returns:
            The title of the currently loaded page.

        Note:
            Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        return await self._invoke_method_async("get_title")

    async def get_user_agent_async(self) -> Optional[str]:
        """
        Returns the value used for the HTTP `User-Agent:` request header.

        Returns:
            The value used for the HTTP `User-Agent:` request header.

        Note:
            Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        return await self._invoke_method_async("get_user_agent")

    def load_file(self, path: str):
        """
        Loads the provided local file.

        Args:
            path: The absolute path to the file.

        Note:
            Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.load_file_async(path))

    async def load_file_async(self, path: str):
        """
        Loads the provided local file.

        Args:
            path: The absolute path to the file.

        Note:
            Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async(
            method_name="load_file",
            arguments={"path": path},
        )

    def load_request(self, url: str, method: RequestMethod = RequestMethod.GET):
        """
        Makes an HTTP request and loads the response in the webview.

        Args:
            url: The URL to load.
            method: The HTTP method to use.
        """
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.load_request_async(url, method))

    async def load_request_async(
        self, url: str, method: RequestMethod = RequestMethod.GET
    ):
        """
        Makes an HTTP request and loads the response in the webview.

        Args:
            url: The URL to load.
            method: The HTTP method to use.

        Note:
            Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async(
            "load_request", arguments={"url": url, "method": method}
        )

    def run_javascript(self, value: str):
        """
        Runs the given JavaScript in the context of the current page.

        Args:
            value: The JavaScript code to run.

        Note:
            Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.run_javascript_async(value))

    async def run_javascript_async(self, value: str):
        """
        Runs the given JavaScript in the context of the current page.

        Args:
            value: The JavaScript code to run.

        Note:
            Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async(
            method_name="run_javascript",
            arguments={"value": value},
        )

    def load_html(self, value: str, base_url: Optional[str] = None):
        """
        Loads the provided HTML string.

        Args:
            value: The HTML string to load.
            base_url: The base URL to use when resolving relative URLs within the value.

        Note:
            Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.load_html_async(value, base_url))

    async def load_html_async(self, value: str, base_url: Optional[str] = None):
        """
        Loads the provided HTML string.

        Args:
            value: The HTML string to load.
            base_url: The base URL to use when resolving relative URLs within the value.

        Note:
            Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async(
            "load_html", arguments={"value": value, "base_url": base_url}
        )

    def scroll_to(self, x: int, y: int):
        """
        Scroll to the provided position of webview pixels.

        Args:
            x: The x-coordinate of the scroll position.
            y: The y-coordinate of the scroll position.

        Note:
            Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.scroll_to_async(x, y))

    async def scroll_to_async(self, x: int, y: int):
        """
        Scroll to the provided position of webview pixels.

        Args:
            x: The x-coordinate of the scroll position.
            y: The y-coordinate of the scroll position.

        Note:
            Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async(
            method_name="scroll_to",
            arguments={"x": x, "y": y},
        )

    def scroll_by(self, x: int, y: int):
        """
        Scroll by the provided number of webview pixels.

        Args:
            x: The number of pixels to scroll by on the x-axis.
            y: The number of pixels to scroll by on the y-axis.

        Note:
            Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        asyncio.create_task(self.scroll_by_async(x, y))

    async def scroll_by_async(self, x: int, y: int):
        """
        Scroll by the provided number of webview pixels.

        Args:
            x: The number of pixels to scroll by on the x-axis.
            y: The number of pixels to scroll by on the y-axis.

        Note:
            Works only on the following platforms: iOS, Android and macOS.
        """
        self._check_mobile_or_mac_platform()
        await self._invoke_method_async(
            method_name="scroll_by",
            arguments={"x": x, "y": y},
        )
