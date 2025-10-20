import 'dart:io' show Platform;
import 'package:flet/flet.dart';
import 'package:flet_webview/src/utils/webview.dart';
import 'package:flutter/material.dart';
import 'package:webview_windows/webview_windows.dart' as windows_webview;

class WebviewDesktop extends StatefulWidget {
  final Control control;

  const WebviewDesktop({Key? key, required this.control}) : super(key: key);

  @override
  State<WebviewDesktop> createState() => _WebviewDesktopState();
}

class _WebviewDesktopState extends State<WebviewDesktop> {
  final windows_webview.WebviewController _controller =
      windows_webview.WebviewController();
  bool _isInitialized = false;
  String? _errorMessage;

  @override
  void initState() {
    super.initState();
    widget.control.addInvokeMethodListener(_invokeMethod);
    
    // Only initialize on Windows
    if (Platform.isWindows) {
      _initializeWebView();
    } else {
      // On Linux, just mark as initialized to show the error message
      setState(() {
        _isInitialized = true;
      });
    }
  }

  Future<void> _initializeWebView() async {
    try {
      await _controller.initialize();
      
      // Set up event listeners
      _controller.url.listen((url) {
        widget.control.triggerEvent("url_change", url);
      });

      _controller.loadingState.listen((state) {
        if (state == windows_webview.LoadingState.loading) {
          widget.control.triggerEvent(
              "page_started", _controller.url.value);
        } else if (state == windows_webview.LoadingState.navigationCompleted) {
          widget.control.triggerEvent(
              "page_ended", _controller.url.value);
        }
      });

      // Load initial URL
      final url = widget.control.getString("url", "https://flet.dev")!;
      await _controller.loadUrl(url);

      // Set background color if specified
      var bgcolor = widget.control.getColor("bgcolor", context);
      if (bgcolor != null) {
        await _controller.setBackgroundColor(bgcolor);
      }

      setState(() {
        _isInitialized = true;
      });
    } catch (e) {
      setState(() {
        _errorMessage = "Failed to initialize WebView: $e";
      });
    }
  }

  Future<dynamic> _invokeMethod(String name, dynamic args) async {
    debugPrint("WebView.$name($args)");
    
    if (!_isInitialized) {
      debugPrint("WebView not initialized, ignoring method call: $name");
      return null;
    }

    switch (name) {
      case "reload":
        await _controller.reload();
        break;
      case "can_go_back":
        return _controller.historyState.value.canGoBack.toString();
      case "can_go_forward":
        return _controller.historyState.value.canGoForward.toString();
      case "go_back":
        await _controller.goBack();
        break;
      case "go_forward":
        await _controller.goForward();
        break;
      case "clear_cache":
        await _controller.clearCache();
        break;
      case "clear_cookies":
        await _controller.clearCookies();
        break;
      case "get_current_url":
        return _controller.url.value;
      case "get_title":
        return _controller.title.value;
      case "load_html":
        await _controller.loadStringContent(args["value"]);
        break;
      case "load_request":
        var url = args["url"];
        if (url != null) {
          await _controller.loadUrl(url);
        }
        break;
      case "run_javascript":
        var javascript = args["value"];
        if (javascript != null) {
          await _controller.executeScript(javascript);
        }
        break;
      case "set_javascript_mode":
        // webview_windows always has JavaScript enabled
        debugPrint("JavaScript mode is always enabled on Windows");
        break;
      default:
        debugPrint("Unknown WebView method: $name");
    }
  }

  @override
  void dispose() {
    debugPrint("WebViewControl dispose: ${widget.control.id}");
    widget.control.removeInvokeMethodListener(_invokeMethod);
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    if (_errorMessage != null) {
      return ErrorControl(_errorMessage!);
    }

    if (!_isInitialized) {
      return const Center(child: CircularProgressIndicator());
    }

    if (Platform.isWindows) {
      return windows_webview.Webview(_controller);
    } else {
      return const ErrorControl(
        "WebView is not yet supported on Linux. "
        "Linux support requires additional system dependencies (webkit2gtk-4.1) "
        "and there are no stable embeddable WebView packages available for Flutter on Linux yet. "
        "For more information, see: https://github.com/flet-dev/flet-webview/issues/17"
      );
    }
  }
}
