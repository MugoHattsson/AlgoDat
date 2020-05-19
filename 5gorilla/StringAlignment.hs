module StringAlignment where
import Data.List (intersperse, elemIndex, groupBy)
import Data.Maybe


scoreMatch = 0
scoreMismatch = -1
scoreSpace = -4
string1 = "writers"
string2 = "vintner"

test1 = "AABC"
test2 = "ABC"
test3 = "ABA"
test4 = "ACA"

list = ['A','B','C']

scoreTable = [[2,0,-1],
              [0,3,1],
              [-1,1,3]]

main = do 
    inp1 <- getLine
    let letters = filter (/=' ') inp1
    nums <- sequence [intLine | _ <- [1..(length letters)]]

    q <- getLine

    inp2 <- sequence [getLine | _ <- [1..(read q :: Int)]]
    let queries = map ((\[a,b] -> (a,b)) . words) inp2

    mapM (`outputOptAlignments` (letters,nums)) queries


intLine :: IO ([Int])
intLine = do 
    line <- getLine
    return $ map read $ words line
 
-- 2.c
maximaBy :: Ord b => (a -> b) -> [a] -> [a]
maximaBy f xs = filter ((maximum (map f xs) ==) . f) xs

-- 2.d
type AlignmentType = (String,String)     
        
type OptEntry = (Int, [AlignmentType])

showAlignment' :: AlignmentType -> String
showAlignment' (a,b) = a ++ " " ++ b

-- 2.e
outputOptAlignments :: (String,String) -> (String, [[Int]]) -> IO ()
outputOptAlignments (xs, ys) (chars,table) = putStrLn . showAlignment' $ head $ optAlignments' xs ys

    where 
        optAlignments' :: String -> String -> [AlignmentType]
        optAlignments' xs ys = snd $ optEntry (length xs) (length ys)
            where
                optEntry i j = buildTable!!i!!j
                buildTable = [[ makeEntry i j | j<-[0..]] | i<-[0..] ]

                makeEntry :: Int -> Int -> OptEntry
                makeEntry 0 0 = (0, [("","")])
                makeEntry i 0 = updateEntry scoreSpace (xs!!(i-1))     '*'     $ optEntry (i-1) 0    
                makeEntry 0 j = updateEntry scoreSpace     '*'     (ys!!(j-1)) $ optEntry 0 (j-1)   
                makeEntry i j = (fst $ head result, concatMap snd result)  
                    where
                        result = maximaBy fst [
                                updateEntry (charScore  x  y)  x  y  (optEntry (i-1) (j-1)),
                                updateEntry (charScore '*' y) '*' y  (optEntry   i   (j-1)),
                                updateEntry (charScore  x '*') x '*' (optEntry (i-1)   j)
                            ]

                        x = xs!!(i-1)
                        y = ys!!(j-1)

                        charScore :: Char -> Char -> Int
                        charScore '*' _  = scoreSpace
                        charScore  _ '*' = scoreSpace 
                        charScore  x  y  = table !! xInd !! yInd
                            where
                                xInd = fromJust $ elemIndex x chars
                                yInd = fromJust $ elemIndex y chars


-- Helper functions for optAlignments'
attachTails :: a -> a -> [([a],[a])] -> [([a],[a])]
attachTails t1 t2 aList = [(xs ++ [t1],ys ++ [t2]) | (xs,ys) <- aList]

updateEntry :: Int -> Char -> Char -> OptEntry -> OptEntry
updateEntry n t1 t2 (s,xs) = (s+n, attachTails t1 t2 xs)                