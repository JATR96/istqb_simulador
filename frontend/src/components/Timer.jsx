import { useEffect, useState } from "react";

/*
|--------------------------------------------------------------------------
| TEMPORIZADOR
|--------------------------------------------------------------------------
*/

function Timer({ initialSeconds, onTimeEnd }) {

  const [seconds, setSeconds] = useState(
    initialSeconds
  );

  useEffect(() => {

    if (seconds <= 0) {

      onTimeEnd();

      return;
    }

    const interval = setInterval(() => {

      setSeconds((prev) => prev - 1);

    }, 1000);

    return () => clearInterval(interval);

  }, [seconds]);

  /*
  |--------------------------------------------------------------------------
  | FORMATO
  |--------------------------------------------------------------------------
  */

  const minutes = Math.floor(seconds / 60);

  const remainingSeconds = seconds % 60;

  return (
    <div className="timer">

      ⏳ {minutes}:
      {remainingSeconds
        .toString()
        .padStart(2, "0")}

    </div>
  );
}

export default Timer;