#!/usr/bin/env python

"""Tests for `hindi_pos_tagger` package."""

from hindi_pos_tagger.hindi_pos_tagger import Main

object_main = Main()

def test_process_word_1():

    word_1 = 'भी'
    pos_1 = 'RP'
    assert object_main.process_word(word_1) == pos_1


def test_process_word_2():

    word_2 = 'कुछ'
    pos_2 = 'QF'
    assert object_main.process_word(word_2) == pos_2

def test_document_Jayasl():

    document_path = './data/Jayasl.txt'
    assert object_main.process_document(document_path) is True

def test_document_Kabeer():

    document_path = './data/Kabeer.txt'
    assert object_main.process_document(document_path) is True

def test_document_Meera():

    document_path = './data/Meera.txt'
    assert object_main.process_document(document_path) is True
