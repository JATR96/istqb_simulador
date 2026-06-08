function ChapterSelector({
  chapters,
  selectedChapters,
  onChange
}) {

  const toggleChapter = (
    chapter
  ) => {

    if (
      selectedChapters.includes(
        chapter
      )
    ) {

      onChange(

        selectedChapters.filter(
          (item) =>
            item !== chapter
        )
      );

      return;
    }

    onChange([
      ...selectedChapters,
      chapter
    ]);
  };

  return (

    <div>

      <h4>
        Capítulos
      </h4>

      {chapters.map(
        (chapter) => (

          <label
            key={chapter}
          >

            <input
              type="checkbox"
              checked={
                selectedChapters.includes(
                  chapter
                )
              }
              onChange={() =>
                toggleChapter(
                  chapter
                )
              }
            />

            {chapter}

          </label>
        )
      )}

    </div>
  );
}

export default ChapterSelector;