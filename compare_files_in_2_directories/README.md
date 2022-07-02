# Compare files in 2 directories

By using this method, we can compare files from 2 sources, including local and remote sources.

## First, output the file system tree information of directory interested into a json file

```{python}
python storeTree.py [target directory path] [output json path]
```

## Second, output the file system tree information of directory interested into a json file

Open the difference.ipynb, change the "dirPath1" and "dirPath2" in chunk 1.
After executing all of the chunks, diff1 and diff2 variables will contain all of the difference.
"diff1" would contains those files only appear in dirPath2, and the files whose size is different from that on dirPath2.
"diff2" is of the same concept.

## [!] Important

"diff1" and "diff2" only contains partial difference because each of them would not record those files that appear only on its directory but not on the other. Therefore, if you really want to find out all of the difference, please check both "diff1" and "diff2".
