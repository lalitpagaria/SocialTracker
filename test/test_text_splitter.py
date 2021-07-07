from obsei.preprocessor.text_splitter import TextSplitterConfig, TextSplitter
from obsei.payload import TextPayload

DOCUMENT_1 = """I love playing console games."""
DOCUMENT_2 = """Beyoncé Giselle Knowles-Carter (/biːˈjɒnseɪ/ bee-YON-say; born September 4, 1981)[6] is an American singer, songwriter, record producer, and actress. Born and raised in Houston, Texas, Beyoncé performed in various singing and dancing competitions as a child. She rose to fame in the late 1990s as the lead singer of Destiny's Child, one of the best-selling girl groups of all time. Their hiatus saw the release of her first solo album, Dangerously in Love (2003), which featured the US Billboard Hot 100 number-one singles "Crazy in Love" and "Baby Boy". Following the 2006 disbandment of Destiny's Child, she released her second solo album, B'Day, which contained hit singles "Irreplaceable" and "Beautiful Liar". Beyoncé also starred in multiple films such as The Pink Panther (2006), Dreamgirls (2006), Obsessed (2009), and The Lion King (2019). Her marriage to Jay-Z and her portrayal of Etta James in Cadillac Records (2008) influenced her third album, I Am... Sasha Fierce (2008), which earned a record-setting six Grammy Awards in 2010. It spawned the successful singles "If I Were a Boy", "Single Ladies (Put a Ring on It)", and "Halo". After splitting from her manager and father Mathew Knowles in 2010, Beyoncé released her musically diverse fourth album 4 in 2011. She later achieved universal acclaim for her sonically experimental visual albums, Beyoncé (2013) and Lemonade (2016), the latter of which was the world's best-selling album of 2016 and the most acclaimed album of her career, exploring themes of infidelity and womanism. In 2018, she released Everything Is Love, a collaborative album with her husband, Jay-Z, as the Carters. As a featured artist, Beyoncé topped the Billboard Hot 100 with the remixes of "Perfect" by Ed Sheeran in 2017 and "Savage" by Megan Thee Stallion in 2020. The same year, she released the musical film and visual album Black Is King to widespread acclaim."""
DOC1_VAL = [29]
DOC2_VAL1 = [503, 512, 504, 384]
DOC2_VAL2 = [503, 512, 507, 505, 394]


def test_no_stride_splits(text_splitter):
    doc1_splits = text_splitter.preprocess_input(
        input_list=[TextPayload(processed_text=DOCUMENT_1)],
        config=TextSplitterConfig(max_split_length=512),
    )

    doc2_splits = text_splitter.preprocess_input(
        input_list=[TextPayload(processed_text=DOCUMENT_2)],
        config=TextSplitterConfig(max_split_length=512),
    )

    assert len(DOC1_VAL) == len(doc1_splits)
    for i, j in zip(doc1_splits, DOC1_VAL):
        assert int(i.meta["text_length"]) == j

    assert len(DOC2_VAL1) == len(doc2_splits)
    for i, j in zip(doc2_splits, DOC2_VAL1):
        assert int(i.meta["text_length"]) == j


def test_stride_splits(text_splitter):
    doc1_splits = text_splitter.preprocess_input(
        input_list=[TextPayload(processed_text=DOCUMENT_1)],
        config=TextSplitterConfig(max_split_length=512, split_stride=128),
    )

    doc2_splits = text_splitter.preprocess_input(
        input_list=[TextPayload(processed_text=DOCUMENT_2)],
        config=TextSplitterConfig(max_split_length=512, split_stride=128),
    )

    assert len(DOC1_VAL) == len(doc1_splits)
    for i, j in zip(doc1_splits, DOC1_VAL):
        assert int(i.meta["text_length"]) == j

    assert len(DOC2_VAL2) == len(doc2_splits)
    for i, j in zip(doc2_splits, DOC2_VAL2):
        assert int(i.meta["text_length"]) == j
