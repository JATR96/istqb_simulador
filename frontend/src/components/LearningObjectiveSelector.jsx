function LearningObjectiveSelector({
  objectives,
  selectedObjectives,
  onChange
}) {

  const toggleObjective = (
    objective
  ) => {

    if (
      selectedObjectives.includes(
        objective
      )
    ) {

      onChange(

        selectedObjectives.filter(
          (item) =>
            item !== objective
        )
      );

      return;
    }

    onChange([
      ...selectedObjectives,
      objective
    ]);
  };

  return (

    <div>

      <h4>
        Learning Objectives
      </h4>

      {objectives.map(
        (objective) => (

          <label
            key={objective}
          >

            <input
              type="checkbox"
              checked={
                selectedObjectives.includes(
                  objective
                )
              }
              onChange={() =>
                toggleObjective(
                  objective
                )
              }
            />

            {objective}

          </label>
        )
      )}

    </div>
  );
}

export default LearningObjectiveSelector;