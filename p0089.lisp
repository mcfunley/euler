(defun mapcn (chars nums string)
  (loop as char across string as i = (position char chars) collect (and i (nth i nums))))
 
(defun parse-roman (R)
  (loop with nums = (mapcn "IVXLCDM" '(1 5 10 50 100 500 1000) R)
        as (A B) on nums if A sum (if (and B (< A B)) (- A) A)))

(defun format-roman (n)
  (if (> n 3999)
      (concatenate 'string "M" (format nil "~@r" (- n 1000)))
    (format nil "~@r" n)))

(let ((chars-saved 0))
  (with-open-file (stream "p089_roman.txt")
                  (do ((line (read-line stream nil)
                             (read-line stream nil)))
                      ((null line))
                    (let* ((roman (format-roman (parse-roman line)))
                           (saved (- (length line) (length roman))))
                      (setq chars-saved (+ chars-saved saved)))))
  (print chars-saved))
