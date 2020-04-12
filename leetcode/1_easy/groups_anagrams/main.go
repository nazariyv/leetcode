package main

// "hash/maphash"
// "strconv"

func id(w *string) int {
	s := 0
	for _, r := range *w {
		s += int(r) * int(r)
	}
	//h := maphash.Hash{}
	//h.Write([]byte(strconv.Itoa(s)))
	return s
}

func main(strs []string) [][]string {
	lives := struct{}{}
	a := make(map[int]map[string]struct{})
	for _, w := range strs {
		_id := id(&w)
		_, exists := a[_id]
		if exists {
			if _, ok := a[_id][w]; !ok {
				a[_id][w] = lives
			}
		} else {
			a[_id] = make(map[string]struct{})
			a[_id][w] = lives
		}
	}

	var o [][]string
	cix := 0
	for _, v := range a {
		o = append(o, []string{})
		for k := range v {
			o[cix] = append(o[cix], k)
		}
		cix++
	}

	return o
}
