from deadlinks.link import Link
from deadlinks.baseurl import BaseURL

import pytest


@pytest.mark.parametrize(
    "url,path", [
        ("https://example.org", ""),
        ("https://example.org/docs/", "/docs/"),
        ("https://example.org/docs/sample.html", "/docs/"),
        ("https://example.org/docs/sample.html/", "/docs/sample.html/"),
    ])
def test_basepath(url, path):
    assert BaseURL(url).get_base_path() == path


@pytest.mark.parametrize(
    "url, internal_link", [
        ("https://example.org/", "https://example.org/index.html"),
        ("https://example.org/docs/", "https://example.org/docs/"),
        ("https://example.org/docs/", "https://example.org/docs/index.html"),
        ("https://example.org/docs/example.html", "https://example.org/docs/index.html"),
        ("https://example.org/docs/example.html", "https://example.org/docs/"),
    ])
def test_basepath_within(url, internal_link):
    assert BaseURL(url).within(Link(internal_link))
    assert BaseURL(internal_link).within(Link(url))


@pytest.mark.parametrize(
    "url, internal_link", [
        ("https://example.org/docs/", "https://example.org/index.html"),
        ("https://example.org/docs/samples/simple.html", "https://example.org/index.html"),
    ])
def test_basepath_within(url, internal_link):
    assert not BaseURL(url).within(Link(internal_link))
    assert BaseURL(internal_link).within(Link(url))


@pytest.mark.parametrize(
    "url, internal_link", [
        ("https://example.org/docs/", "https://example.net/docs/"),
    ])
def test_basepath_within_extranal(url, internal_link):
    assert not BaseURL(url).within(Link(internal_link))
    assert not BaseURL(internal_link).within(Link(url))
