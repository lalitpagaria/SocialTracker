import pytest

from obsei.analyzer.classification_analyzer import ZeroShotClassificationAnalyzer
from obsei.analyzer.ner_analyzer import NERAnalyzer
from obsei.analyzer.pii_analyzer import (
    PresidioEngineConfig,
    PresidioModelConfig,
    PresidioPIIAnalyzer,
)
from obsei.analyzer.sentiment_analyzer import VaderSentimentAnalyzer
from obsei.analyzer.translation_analyzer import TranslationAnalyzer
from obsei.preprocessor.text_cleaner import TextCleaner
from obsei.preprocessor.text_splitter import TextSplitterConfig, TextSplitter


@pytest.fixture(scope="session")
def zero_shot_analyzer():
    return ZeroShotClassificationAnalyzer(
        model_name_or_path="typeform/mobilebert-uncased-mnli",
    )


@pytest.fixture(scope="session")
def vader_analyzer():
    return VaderSentimentAnalyzer()


@pytest.fixture(scope="session")
def ner_analyzer():
    return NERAnalyzer(
        model_name_or_path="dbmdz/bert-large-cased-finetuned-conll03-english",
        tokenizer_name="bert-base-cased",
    )


@pytest.fixture(scope="session")
def translate_analyzer():
    return TranslationAnalyzer(
        model_name_or_path="Helsinki-NLP/opus-mt-hi-en", batch_size=1
    )


@pytest.fixture(scope="session")
def pii_analyzer():
    return PresidioPIIAnalyzer(
        engine_config=PresidioEngineConfig(
            nlp_engine_name="spacy",
            models=[PresidioModelConfig(model_name="en_core_web_lg", lang_code="en")],
        )
    )


@pytest.fixture(scope="session")
def text_cleaner():
    return TextCleaner()


@pytest.fixture(scope="session")
def text_splitter():
    return TextSplitter()
