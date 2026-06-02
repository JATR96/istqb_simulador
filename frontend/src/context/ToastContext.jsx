import {
  createContext,
  useState
} from "react";

import Toast from "../components/Toast";

export const ToastContext =
  createContext();

export function ToastProvider({
  children
}) {

  const [toast, setToast] =
    useState(null);

  /*
  |--------------------------------------------------------------------------
  | SHOW TOAST
  |--------------------------------------------------------------------------
  */

  const showToast = (
    message
  ) => {

    setToast(message);

    setTimeout(() => {

      setToast(null);

    }, 3000);
  };

  return (
    <ToastContext.Provider
      value={{
        showToast
      }}
    >

      {children}

      {toast && (
        <Toast
          message={toast}
        />
      )}

    </ToastContext.Provider>
  );
}