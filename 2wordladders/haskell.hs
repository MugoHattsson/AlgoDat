module Main where
import Data.List hiding (lookup)
import Data.Sequence hiding (lookup)
import Data.Maybe
import Control.Monad


main = do 
    line <- getLine
    let args = words line

    keys <- sequenceLines (read $ head args)
    queries <- sequenceLines (read $ last args)

    let graph = buildGraph keys
        formatQueries = map ((\xs -> (head xs, last xs)) . words) queries

    --mapM_ print graph
    bfsLoop formatQueries graph

    where 
        sequenceLines n = sequence [getLine | x <- [1..n]]
   

buildGraph xs = [(w, findNeighbours w xs) | w <- xs] 

findNeighbours :: String -> [String] -> [String]
findNeighbours w xs = [x | x <- xs, x /= w && (tail w) `contained` x]

contained :: String -> String -> Bool
contained [] [c] = True
contained []  _  = False
contained  _  [] = False
contained (x:xs) ys = contained xs (delete x ys)

type Graph = [(String,[String])]

bfsLoop :: [(String,String)] -> Graph -> IO () 
bfsLoop [] _ = return ()
bfsLoop (q:qs) graph = do
    let start = fst q
        queue = fromList [start]
    --print q
    bfs q graph queue [start] [(start,"")]
    bfsLoop qs graph

bfs :: (String,String) -> Graph -> Seq String -> [String] -> [(String,String)] -> IO ()
bfs   _   _   _      []  _ = putStrLn "Impossible" 
bfs (s,e) _   _      [w] _ | s == e = putStrLn "0"
bfs   _   _ Empty     _  _ = putStrLn "Impossible"
bfs (_,e) g (q:<|qs)  v  p = do 
    -- putStrLn ""
    -- putStrLn "bfs"
    -- putStrLn $ "Q: " ++ show (q:<|qs)
    search (q,e) (lookup q g) (qs) v p 
    -- putStrLn ""

    where
        search :: (String,String) -> Maybe [String] -> Seq String -> [String] -> [(String,String)] -> IO ()
        search (c,e) (Just [])     qs vs ps = bfs (c,e) g qs vs ps 
        search (c,e) (Just (n:ns)) qs vs ps = do
            --putStrLn $ "Search: " ++ (show [c,e,n])
            if n `notElem` vs then do
                
                --putStrLn $ "Q':" ++ show qs'
                if n == e then do 
                    print (pathLength n ps' 0) 
                    else 
                        search (c,e) (Just ns) qs' vs' ps'
                else if (ns == []) then bfs (c,e) g qs vs ps 
                    else search (c,e) (Just ns) qs vs ps 
            where
                vs' = n : vs
                qs' = qs |> n 
                ps' = (n,c) : ps 

pathLength :: String -> [(String,String)] -> Int -> Int
pathLength n ps l 
    | p == ("") = l
    | otherwise = pathLength p ps (l+1)
    where 
        p = fromJust $ lookup n ps